from flask import Flask, request, render_template
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

# handle 404
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', title='404', message='page not found'), 404

# unhandled errors
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('error.html', message='internal server error'), 500