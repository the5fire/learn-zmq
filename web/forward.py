"""
@the5fire

接受publisher的消息，转发给server
"""

import zmq

sub_port = "5555"
pub_port = '5556'

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
sub_socket.setsockopt(zmq.SUBSCRIBE, b'')
sub_socket.bind("tcp://*:%s" % sub_port)

pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://*:%s" % pub_port)


while True:
    zmq.device(zmq.FORWARDER, sub_socket, pub_socket)
