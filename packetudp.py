import socket

UDP_IP = "10.0.1.137"
UDP_PORT = 46481
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

i=0
while i==0:
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
