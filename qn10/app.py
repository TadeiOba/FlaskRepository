# app/__init__.py

from flask import Flask, render_template

app = Flask(__name__)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Main route
@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
