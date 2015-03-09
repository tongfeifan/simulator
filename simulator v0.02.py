# author: Feifan Tong
# coding: utf8
from Queue import Queue
import string
import time

def creatOrder(file_line):
	list = string.split(str(file_line.rstrip('\n')) , ",")
	order = Order()
	print list
	order.ID = list[0]
	order.time = int(list[1])
	return order


class Trader:
	"""docstring for Trader"""
	def __init__(self, ID):
		self.order_queue = Queue()
		self.ID = ID
		self.next_time = 0
		self.order = Order()
		self.number_of_order = 0

	def sendOrder(self, exchange, time):
		exchange.receiveOrder(self.order,time)
		print "send order:"+str(self.order.ID)
		if self.order_queue.empty() == False:
			self.order = self.order_queue.get()
			self.next_time = self.next_time + self.order.time
		else :
			if self.number_of_order != 0:
				self.number_of_order = self.number_of_order - 1

	def readOrder(self):
		print "readfile" + str(self.ID) + "..."
		f = open("trader"+str(self.ID)+".csv" , "r")
		for line in f:
			temp_order = creatOrder(line)
			self.order_queue.put(temp_order)
		f.close()
		self.order = self.order_queue.get()
		self.next_time = self.next_time + self.order.time
		self.number_of_order = 1

	def isEmpty(self):
		if self.number_of_order != 0 :
			return False
		else :
			return True


class Exchange:
	"""docstring for Exchange"""
	def __init__(self, ID):
		self.order_queue = Queue()
		self.ID = ID

	def receiveOrder(self, order, time):
		order.timestamp = time
		self.order_queue.put(order)

	def sendOrder():
		pass

	def isEmpty(self):
		return self.order_queue.empty()
		
class Order:
	"""docstring for Order"""
	def __init__(self ):
		self.ID = ""
		self.time = 0
		self.timestamp = ""

class Market:
	"""docstring for Market"""
	def __init__(self):
		self.time = 0
		self.trader1 = Trader(1)
		self.trader2 = Trader(2)
		self.exchange1 = Exchange(1)

	def start(self):
		self.trader1.readOrder()
		self.trader2.readOrder()
		print "reading finished\n"

	def simulate(self):
		self.traderToExchange()
		self.exchangeToOutput()

	def traderToExchange(self):
		while self.trader1.isEmpty() == False and self.trader2.isEmpty() == False:
			if self.trader1.next_time < self.trader2.next_time:
				self.time = self.trader1.next_time
				self.trader1.sendOrder(self.exchange1, self.time)
			else :
				self.time = self.trader2.next_time
				self.trader2.sendOrder(self.exchange1, self.time)
		if self.trader1.isEmpty():
			while self.trader2.isEmpty() == False:
				self.time = self.trader2.next_time
				self.trader2.sendOrder(self.exchange1, self.time)
		else :
			while self.trader1.isEmpty() == False:
				self.time = self.trader1.next_time
				self.trader1.sendOrder(self.exchange1, self.time)

	def exchangeToOutput(self):
		f = open ("output.csv" , "w")
		f.write("orderID,orderTime,orderTimeStamp\n")
		while self.exchange1.isEmpty() == False:
			head_order = self.exchange1.order_queue.get()
			f.write(str(head_order.ID)+","+str(head_order.time)+","+str(head_order.timestamp)+"\n")
		f.close()

m = Market()
m.start()
m.simulate()
		
		



