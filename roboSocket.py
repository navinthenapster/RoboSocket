from socketIO_client_nexus import SocketIO
import time
from multiprocessing import Process

'''
@TO-DO
  -[] Implementing the logging
  -[] custom connect field
  -[] Custom Exception
  -[] Check The Add event to the Listener
  -[] Create a Server class 
  -[] Integrate the signals with the socket

'''

socket = None

def on_connect():
	global socket	
	print "Connected"
	socket.emit('connect',10)

def on_status(arg):
	print ("status received")

def on_eyes(arg):
	print ("eyes received")

def on_servos(arg):
	print ("servos received")

def on_logs(arg):
	print ("logs received")
	

class Listener():

	socket=None
	process=None

	def __init__(self,**kwargs):
		self.socket = SocketIO('127.0.0.1', 8000)	
		self.socket.on('connect', on_connect)
		self.socket.on('eyes', on_eyes)
		self.socket.on('status', on_status)
		self.socket.on('servos', on_servos)
		self.socket.on('logs', on_logs)

	def add_event(self,event_name,event_function):
		if self.socket is None:
			print ("socket is not initialized")
		if callable(event_function):
			self.socket.on(event_name,event_function)
		else:
			print("UnCallable Function")	

	def run(self):
		'''	
		Run the socket and block the program execution
		'''
		if self.socket is not None:
			print("[Status] : RoboSocket listener connected")
			self.socket.wait()

	def connect(self):
		'''
		Run the socket parallel and non block the program
		'''
		self.process = Process(target=self.run(),args=())
		self.process.start()
		return

if __name__ == "__main__":
	print (" **** Testing : Checking Listener *****")
	listener=Listener()	
	#listener.connect(host="127.0.0.1",port=8000)
	listener.connect()
	
	

