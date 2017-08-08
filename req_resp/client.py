import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(1, 10):
    print('sending request', request)
    socket.send(b'hello')

    msg = socket.recv()
    print('Received reply ', request, '[', msg, ']')
