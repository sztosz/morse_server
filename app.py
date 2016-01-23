import time
import zmq

from flask import Flask, render_template, request

app = Flask(__name__)
port = "5556"


@app.route('/', methods=['GET', 'POST'])
def upload():
    message = None
    if request.method == 'POST':
        try:
            context = zmq.Context()
            socket = context.socket(zmq.PUB)
            socket.bind("tcp://*:{}".format(port))
            time.sleep(1)
            socket.send_string('Morse ' + request.form['morse'])
            message = request.form['morse']
        except Exception as e:
            message = e
    return render_template('form.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
