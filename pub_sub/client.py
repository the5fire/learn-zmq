import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)


# Subscribe to zipcode, default is NYC, 10001
topicfilter = b"10001"
socket.setsockopt(zmq.RCVTIMEO, -1)
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
# socket.setsockopt(zmq.RCVTIMEO, b'30000')

# Process 5 updates
total_value = 0
while True:
    # string = socket.recv()
    print('in loop')
    routing_key, *args = socket.recv_multipart()

    print(routing_key, args)
