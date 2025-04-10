from flask import Flask, render_template
from flask_socketio import SocketIO, send
from cryptography.fernet import Fernet

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Encryption key
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/receiver")
def receiver():
    return render_template("receiver.html")

@socketio.on("message")
def handle_message(data):
    encrypted_message = cipher_suite.encrypt(data["message"].encode()).decode()
    send({"user": data["user"], "message": data["message"], "encrypted": encrypted_message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5500, debug=True)
