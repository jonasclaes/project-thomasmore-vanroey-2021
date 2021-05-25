from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/pagina1")
def pagina1():
    return render_template("page1.html")


@socketio.on('message')
def handle_message(data):
    print('received message: ' + str(data))
    send(data)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send(json, json=True, broadcast=True)


@socketio.on('change window')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    send(json, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
