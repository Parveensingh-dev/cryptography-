from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import base64

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def decrypt_message(encrypted_msg):
    return base64.b64decode(encrypted_msg.encode()).decode()

@app.route("/")
def receiver():
    return render_template("receiver.html")

@socketio.on("message")
def handle_message(data):
    encrypted_msg = data.get("encrypted")
    decrypted_msg = decrypt_message(encrypted_msg)
    print(f"Received Encrypted: {encrypted_msg}")
    print(f"Decrypted Message: {decrypted_msg}")

    # Send the received message to receiver UI
    emit("message", {"decrypted": decrypted_msg, "encrypted": encrypted_msg}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5001, debug=True)
