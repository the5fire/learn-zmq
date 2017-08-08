import json
import time

import zmq

port = "5555"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:%s" % port)


counter = 1
while True:
    print('send')
    data = json.dumps({'name': 'huyaaaaa.{}'.format(counter)})
    data = data.encode()
    socket.send_multipart((b'change', data))
    time.sleep(1)
    counter += 1
