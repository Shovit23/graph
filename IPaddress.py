import socket
hostname = socket.gethostname()
IpAddr = socket.gethostbyname(hostname)
print('my ip address is '+IpAddr)