
# example from zmq page

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

# import time
# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

# while True:
#     #  Wait for next request from client
#     message = socket.recv()
#     print("Received request: %s" % message)

#     #  Do some 'work'
#     time.sleep(1)

#     #  Send reply back to client
#     socket.send(b"World")

import zmq
# from zmq.sugar import context, socket

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://127.0.0.1:8000")


while True:
    msg = socket.recv_string()
    print("Client Request: ", msg)
    smsg = input('Server Reply: ')
    # print(b'smsg')
    socket.send_string(smsg)
    print("---")

