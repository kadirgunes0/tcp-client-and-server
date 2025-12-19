import socket

ip = input("ip veya url giriniz: ")
port = 80

client = socket.scoket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ip, port)

client.send(b"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n")

response = client.recv(4096)

print(response.decode())