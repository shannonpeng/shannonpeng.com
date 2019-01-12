from flask import Flask, request, render_template, render_template_string, url_for, redirect, session, flash
from flask_pymongo import PyMongo
from bson import objectid
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_flatpages import FlatPages, pygments_style_defs
from markdown2 import Markdown
from .user import User
import os, requests

# set up flask app and connect to database
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET')
app.config['MONGO_URI'] = os.environ.get('MONGOLAB_URI')
mongo = PyMongo(app)

# set up project posts
markdowner = Markdown(extras=['fenced-code-blocks', 'target-blank-links' , 'markdown-in-html'])
def my_renderer(text):
    prerendered_body = render_template_string(text)
    return markdowner.convert(prerendered_body)
DEBUG = os.environ.get('FLASK_ENV') == 'development'
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'projects'
app.config['FLATPAGES_HTML_RENDERER'] = my_renderer
app.config.from_object(__name__)
flatpages = FlatPages(app)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You gotta log in to do that. 😤'
@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({ 'username': username })
    if not user:
        return None
    return User(user['username'])

# home/projects page
@app.route('/')
def index():
    featured_projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR) and p.meta.get('featured') is True and p.meta.get('hidden') is None], key=lambda x:x['date'], reverse=True)
    projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR) and p.meta.get('featured') is None and p.meta.get('hidden') is None], key=lambda x:x['date'], reverse=True)
    stats = get_stats()
    return render_template('index.html', projects=featured_projects+projects, stats=stats, page='projects')

# classes page
@app.route('/classes')
def classes():
    stats = get_stats()
    return render_template('classes.html', stats=stats, page='classes')

# photos page
@app.route('/photos')
def photos():
    stats = get_stats()
    photo_count = 18
    response = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token={0}&count={1}'.format(os.environ.get('IG_ACCESS_TOKEN'), photo_count)).json()
    recent_media = response.get('data') or []
    return render_template('photos.html', photos=recent_media, stats=stats, page='photos')

# go links
@app.route('/go/<keyword>')
def go_get(keyword):
    link = mongo.db.links.find_one_or_404({ 'keyword': keyword })
    url = link.get('url')
    if url.find('//') < 0:
        return redirect('//' + url)
    return redirect(url)

@app.route('/go/create', methods=['POST'])
@login_required
def go_create():
    keyword = request.form.get('keyword')
    url = request.form.get('url')
    if keyword and url:
        new_link = { 'keyword': keyword, 'url': url }
        result = mongo.db.links.replace_one({ 'keyword': keyword }, new_link, upsert=True)
        if result.acknowledged:
            flash('Link created successfully 😍', category='success')
        else:
            flash('Link not created. 😬', category='error')
    else:
        flash('Keyword or URL missing. 🤔', category='error')
    return redirect(url_for('admin'))

@app.route('/go/delete', methods=['POST'])
@login_required
def go_delete():
    link_id = request.form.get('link_id')
    link = mongo.db.links.find_one_and_delete({ '_id': objectid.ObjectId(link_id) })
    if link:
        flash('Link deleted successfully 💨', category='success')
    else:
        flash('Link not deleted. 😬', category='error')
    return redirect(url_for('admin'))

# sessions and admin portal
@app.route('/admin')
@login_required
def admin():
    links = sorted(mongo.db.links.find(), key=lambda x: x['keyword'])
    stats = get_stats()
    return render_template('admin.html', stats=stats, links=links)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': # return login page
        if not session.get('user_id'):
            return render_template('login.html')
        return redirect(url_for('admin'))
    elif request.method == 'POST': # authenticate and redirect to portal
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = mongo.db.users.find_one({ 'username': username })
            if user and User.validate_login(user['password'], password):
                user_obj = User(user['username'])
                login_user(user_obj)
                return redirect(request.args.get('next') or url_for('admin'))
        flash('Invalid username or password 🙅‍♀️', category='error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    flash('You\'re logged out. Buh-bye. ✌️', category='message')
    return redirect(url_for('index'))

# stats

LAST_FM_API_KEY = os.environ.get('LAST_FM_API_KEY')
LAST_FM_USERNAME = 'spenguinx'

def get_stats():
    order = ['status', 'song', 'movie']
    # fetch latest song from last fm API and update database
    data = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={0}&api_key={1}&limit=1&format=json'.format(LAST_FM_USERNAME, LAST_FM_API_KEY)).json()
    song = data['recenttracks']['track'][0]
    song_title = song['name']
    song_artist = song['artist']['#text']
    song_url = song['url']
    song_live = '@attr' in song and song['@attr']['nowplaying'] == 'true'
    update_stat('song', { "title": song_title, "artist": song_artist, "live": song_live, "url": song_url })
    try:
        stats = sorted(mongo.db.stats.find() or [], key=lambda stat: order.index(stat['name']))
    except:
        stats = sorted(mongo.db.stats.find() or [], key=lambda stat: stat['name'], reverse=True)
    return stats
def get_stat_by_name(name):
    return mongo.db.stats.find_one({ "name": name })
def update_stat(name, fields):
    s = get_stat_by_name(name)
    if s:
        for k in s:
            if k in fields:
                s[k] = fields[k]
        result = mongo.db.stats.replace_one({ 'name': name }, s, upsert=False)
        return result
    return False

@app.route('/stats/<name>', methods=['POST'])
@login_required
def stats(name):
    form = dict(request.form)
    s = get_stat_by_name(name)
    if s:
        for k in s:
            if k in form:
                if type(form[k]) == list and not (len(form[k]) == 0 or len(form[k][0]) == 0):
                    s[k] = form[k][0]
                elif not type(form[k]) == list:
                    s[k] = form[k]
        result = mongo.db.stats.replace_one({ 'name': name }, s, upsert=False)
        if result.acknowledged:
            flash('Stat updated successfully 😍', category='success')
        else:
            flash('Stat not updated. 😬', category='error')
    else:
        flash('The requested stat was not found. 🙊', category='error')
    return redirect(url_for('admin'))

# project posts
@app.route('/projects/<name>', strict_slashes=False)
def project(name):
    path = '{}/{}'.format(POST_DIR, name)
    project = flatpages.get_or_404(path)
    return render_template('project.html', project=project)

# handle 404
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', title='404', message='page not found 👻'), 404

# unhandled errors
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('error.html', message='internal server error ⚠️'), 500