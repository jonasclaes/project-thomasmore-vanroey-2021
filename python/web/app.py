from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/page14")
def hello_world():
    return render_template("index_local.html")


@app.route("/page5")
def page1():
    return render_template("Milestone1.html")


@app.route("/page4")
def page2():
    return render_template("Milestone2.html")


@app.route("/page3")
def page3():
    return render_template("Milestone3.html")


@app.route("/page2")
def page4():
    return render_template("Milestone4.html")


@app.route("/page1")
def page5():
    return render_template("Milestone5.html")


@app.route("/page12")
def page6():
    return render_template("Milestone6.html")


@app.route("/page11")
def page7():
    return render_template("Milestone7.html")


@app.route("/page10")
def page8():
    return render_template("Milestone8.html")


@app.route("/page9")
def page9():
    return render_template("Milestone9.html")


@app.route("/page8")
def page10():
    return render_template("Milestone10.html")


@app.route("/page7")
def page11():
    return render_template("Photo.html")


@app.route("/page6")
def page12():
    return render_template("comingsoon.html")


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
