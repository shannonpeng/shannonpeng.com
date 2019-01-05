from flask import Flask, request, render_template, url_for, redirect, session, flash
from flask_pymongo import PyMongo
from bson import objectid
from flask_login import LoginManager, login_required, login_user, logout_user
from .user import User
import os

# set up flask app and connect to database
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET')
app.config['MONGO_URI'] = os.environ.get('MONGOLAB_URI')
mongo = PyMongo(app)

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You must log in to continue.'
@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({ 'username': username })
    if not user:
        return None
    return User(user['username'])

# home page
@app.route('/')
def index():
    return render_template('index.html')

# go links
@app.route('/go/<keyword>')
def go_get(keyword):
    link = mongo.db.links.find_one_or_404({ 'keyword': keyword })
    return redirect(link.get('target'))

@app.route('/go/create', methods=['POST'])
@login_required
def go_create():
    keyword = request.form.get('keyword')
    target = request.form.get('target')
    if keyword and target:
        new_link = { 'keyword': keyword, 'target': target }
        result = mongo.db.links.replace_one({ 'keyword': keyword }, new_link, upsert=True)
        if result.acknowledged:
            flash('Link created successfully', category='success')
        else:
            flash('Link not created.', category='error')
    return redirect(url_for('admin'))

@app.route('/go/delete', methods=['POST'])
@login_required
def go_delete():
    link_id = request.form.get('link_id')
    link = mongo.db.links.find_one_and_delete({ '_id': objectid.ObjectId(link_id) })
    if link:
        flash('Link deleted successfully', category='success')
    else:
        flash('Link not deleted.', category='error')
    return redirect(url_for('admin'))

# sessions and admin portal
@app.route('/admin')
@login_required
def admin():
    links = mongo.db.links.find()
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
        flash('Invalid username or password', category='error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# TODO: fun stats [last.fm, instagram, book, movie]

# TODO: project writeup routing

# handle 404
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', title='404', message='page not found'), 404

# unhandled errors
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('error.html', message='internal server error'), 500