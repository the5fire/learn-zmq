import json
import threading

import zmq

from flask import Flask
app = Flask(__name__)


class Config:
    notstart = True


CACHE = {
    'name': 'the5fire'
}


@app.route("/")
def hello():
    if Config.notstart:
        listen_thread = threading.Thread(target=listen, args=('cache', CACHE))
        listen_thread.daemon = True
        listen_thread.start()
        Config.notstart = False

    return "Hello World - from {name}".format(**CACHE)


def listen(key, target):
    print(key, target)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    print("waiting for update cache")
    socket.connect("tcp://localhost:%s" % 5556)
    socket.setsockopt(zmq.RCVTIMEO, -1)
    socket.setsockopt(zmq.SUBSCRIBE, b'change')

    while True:
        print('in loop')
        name, value = socket.recv_multipart()
        print(name, value)
        value = json.loads(value)
        target.update(value)
        break


if __name__ == '__main__':
    app.run()
