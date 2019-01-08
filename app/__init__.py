from flask import Flask, request, render_template, url_for, redirect, session, flash
from flask_pymongo import PyMongo
from bson import objectid
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_flatpages import FlatPages
from .user import User
import os

# set up flask app and connect to database
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET')
app.config['MONGO_URI'] = os.environ.get('MONGOLAB_URI')
mongo = PyMongo(app)

# set up project posts
DEBUG = os.environ.get('FLASK_ENV') == 'development'
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'projects'
app.config.from_object(__name__)
flatpages = FlatPages(app)

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Nice try, hacker. 😤'
@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({ 'username': username })
    if not user:
        return None
    return User(user['username'])

# home page [projects]
@app.route('/')
def index():
    projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR)], key=lambda x:x['date'], reverse=True)
    return render_template('index.html', projects=projects, page='projects')

# classes page
@app.route('/classes')
def classes():
    projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR)], key=lambda x:x['date'], reverse=True)
    return render_template('classes.html', page='classes')

# photos page
@app.route('/photos')
def photos():
    projects = sorted([p for p in flatpages if p.path.startswith(POST_DIR)], key=lambda x:x['date'], reverse=True)
    return render_template('index.html', projects=projects, page='photos')

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
    return render_template('admin.html', links=links)

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

# TODO: fun stats [last.fm, instagram, book, movie]

# project posts
@app.route('/projects/<name>')
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