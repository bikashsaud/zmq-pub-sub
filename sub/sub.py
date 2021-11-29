

#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back


# import zmq

# context = zmq.Context()

# #  Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

# #  Do 10 requests, waiting each time for a response
# for request in range(10):
#     print("Sending request %s …" % request)
#     socket.send(b"Hello")

#     #  Get the reply.
#     message = socket.recv()
#     print("Received reply %s [ %s ]" % (request, message)) 


import zmq 
context = zmq.Context()

print("connecting to server")
socket = context.socket(zmq.REQ)

socket.connect("tcp://127.0.0.1:9000")

while True:
    cmsg = input("Enter Request Message: ")
    socket.send_string(cmsg)
    # print('sending...', cmsg)
    print("From Server: ", socket.recv_string())
    print("---")
