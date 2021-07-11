import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HEADERSIZE = 10
# Now, since this is the client, rather than binding, we are going to connect.
s.connect((socket.gethostname(), 1234))
# In the more traditional sense of client and server, you wouldnt actually have the client and server on the same machine. If you wanted to have two programs talking to eachother locally, you could do this, but typically your client will more likely connect to some external server, using its public IP address, not socket.gethostname(). You will pass the string of the IP instead.

# # Our sockets can send and recv data. These methods of handling data deal in buffers. Buffers happen in chunks of data of some fixed size
# msg = s.recv(1024)
# # This means our socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time.
# print(msg.decode("utf-8"))


while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""