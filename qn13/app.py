# app/__init__.py

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('notification')
def handle_notification(data):
    emit('receive_notification', data, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Database created successfully")
        except Exception as e:
            print(f"Error creating database: {str(e)}")
    socketio.run(app, debug=False)
    #app.run(host="0.0.0.0", port=5002)
