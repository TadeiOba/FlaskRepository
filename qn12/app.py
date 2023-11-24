# app/__init__.py

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
socketio = SocketIO(app)
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=dt.utcnow)

@socketio.on('update_data')
def handle_update_data(data):
    socketio.emit('data_updated', data, broadcast=True)

    new_data = Data(value=data)
    db.session.add(new_data)
    db.session.commit()

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
