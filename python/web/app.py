from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/pagina14")
def hello_world():
    return render_template("index.html")


@app.route("/pagina1")
def pagina1():
    return render_template("page1.html")


@app.route("/pagina2")
def pagina2():
    return render_template("page2.html")


@app.route("/pagina3")
def pagina3():
    return render_template("page3.html")


@app.route("/pagina4")
def pagina4():
    return render_template("page4.html")


@app.route("/pagina5")
def pagina5():
    return render_template("page5.html")


@app.route("/pagina6")
def pagina6():
    return render_template("page6.html")


@app.route("/pagina7")
def pagina7():
    return render_template("page7.html")


@app.route("/pagina8")
def pagina8():
    return render_template("page8.html")


@app.route("/pagina9")
def pagina9():
    return render_template("page9.html")


@app.route("/pagina10")
def pagina10():
    return render_template("page10.html")


@app.route("/pagina11")
def pagina11():
    return render_template("page11.html")


@app.route("/pagina12")
def pagina12():
    return render_template("page12.html")


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
