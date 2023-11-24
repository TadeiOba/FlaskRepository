from flask import Flask, render_template, redirect, url_for, request
from flask import flash
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Message:', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=False)
    app.run(host="0.0.0.0", port=5002)
