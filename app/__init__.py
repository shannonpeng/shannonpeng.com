from flask import Flask, request, render_template, render_template_string, url_for, redirect, session, flash
from flask_pymongo import PyMongo
from bson import objectid
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_flatpages import FlatPages, pygments_style_defs
from markdown2 import Markdown
from .user import User
import os, requests


#******************
#***** SETUP ******
#******************

# setup Flask app and connect to mLab database
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET')
app.config['MONGO_URI'] = os.environ.get('MONGOLAB_URI')
mongo = PyMongo(app)

# setup Flatpages renderer for project posts
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
login_manager.login_message = 'you gotta log in to do that. 😤'

@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({ 'username': username })
    if not user:
        return None
    return User(user['username'])


#*******************
#***** ROUTES ******
#*******************

# home page (projects)
@app.route('/')
def index():
    featured_projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR) and p.meta.get('featured') is True and p.meta.get('hidden') is None], key=lambda x:x['date'], reverse=True)
    projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR) and p.meta.get('featured') is None and p.meta.get('hidden') is None], key=lambda x:x['date'], reverse=True)
    return render_template('index.html', projects=featured_projects+projects, page='projects')

# classes page
@app.route('/classes')
def classes():
    return render_template('classes.html', page='classes')

# about page
@app.route('/about')
def about():
    stats = get_stats()
    return render_template('about.html', stats=stats, page='about')

# project pages
@app.route('/projects/<name>', strict_slashes=False)
def project(name):
    path = '{}/{}'.format(POST_DIR, name)
    project = flatpages.get_or_404(path)
    return render_template('project.html', project=project)


#*********************
#***** GO LINKS ******
#*********************

# fetch go link
@app.route('/go/<keyword>')
def go_get(keyword):
    link = mongo.db.links.find_one_or_404({ 'keyword': keyword })
    url = link.get('url')
    if url.find('//') < 0:
        return redirect('//' + url)
    return redirect(url)

# create new go link
@app.route('/go/create', methods=['POST'])
@login_required
def go_create():
    keyword = request.form.get('keyword')
    url = request.form.get('url')
    if keyword and url:
        new_link = { 'keyword': keyword, 'url': url }
        result = mongo.db.links.replace_one({ 'keyword': keyword }, new_link, upsert=True)
        if result.acknowledged:
            flash('link created successfully 👏', category='success')
        else:
            flash('link not created. 😬', category='error')
    else:
        flash('link keyword or URL missing. 🤔', category='error')
    return redirect(url_for('admin'))

# delete a go link
@app.route('/go/delete', methods=['POST'])
@login_required
def go_delete():
    link_id = request.form.get('link_id')
    link = mongo.db.links.find_one_and_delete({ '_id': objectid.ObjectId(link_id) })
    if link:
        flash('link deleted successfully 💨', category='success')
    else:
        flash('link not deleted. 😬', category='error')
    return redirect(url_for('admin'))


#**************************************
#***** SESSIONS AND ADMIN PORTAL ******
#**************************************

# admin portal route
@app.route('/admin')
@login_required
def admin():
    links = sorted(mongo.db.links.find(), key=lambda x: x['keyword'])
    stats = get_stats()
    return render_template('admin.html', stats=stats, links=links)

# login route
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
        flash('invalid username or password 🙅‍♀️', category='error')
        return redirect(url_for('login'))

# logout route
@app.route('/logout')
def logout():
    logout_user()
    flash('you\'re logged out. Buh-bye. ✌️', category='message')
    return redirect(url_for('index'))


#******************************
#***** STATS (FUN FACTS) ******
#******************************

LAST_FM_API_KEY = os.environ.get('LAST_FM_API_KEY')
LAST_FM_USERNAME = os.environ.get('LAST_FM_USERNAME')

def get_stats():
    order = ['status', 'song', 'movie']
    # fetch latest song from last fm API and update database
    data = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={0}&api_key={1}&limit=1&format=json'.format(LAST_FM_USERNAME, LAST_FM_API_KEY)).json()
    try:
        song = data['recenttracks']['track'][0]
        song_title = song['name']
        song_artist = song['artist']['#text']
        song_url = song['url']
        song_live = '@attr' in song and song['@attr']['nowplaying'] == 'true'
        update_stat('song', { 'title': song_title, 'artist': song_artist, 'live': song_live, 'url': song_url })
    except:
        pass
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
        for k in fields:
            if k in s and len(str(fields[k]).strip()) > 0:
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
                if type(form[k]) == list and not len(form[k]) == 0 and not len(form[k][0]) == 0:
                    s[k] = form[k][0]
                elif not type(form[k]) == list:
                    s[k] = form[k]
        result = mongo.db.stats.replace_one({ 'name': name }, s, upsert=False)
        if result.acknowledged:
            flash('stat updated successfully 👏', category='success')
        else:
            flash('stat not updated. 😬', category='error')
    else:
        flash('the requested stat was not found. 🙊', category='error')
    return redirect(url_for('admin'))


#***************************
#***** ERROR HANDLING ******
#***************************

# handle 404
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', title='404', message='that page doesn\'t exist 👽'), 404

# unhandled errors
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('error.html', message='yikes... internal server error ⚠️'), 500