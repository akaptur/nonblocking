import socket
import time

def send_slowly(hostname, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hostname, port))
	s.sendall("Hello")
	time.sleep(30)  # hang
	msg = s.recv(1028)  
	print msg

if __name__ == '__main__':
	send_slowly('127.0.0.1', 1060)