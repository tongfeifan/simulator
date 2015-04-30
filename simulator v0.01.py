# author: Feifan Tong
# coding: utf8
from Queue import Queue
import string

def creatOrder(file_line):
	list = string.split(str(file_line.rstrip('\n')) , ",")
	order = Order()
	print list
	order.ID = list[0]
	order.time = list[1]
	return order


class Trader:
	"""docstring for Trader"""
	def __init__(self, ID):
		self.order_queue = OrderQueue()
		self.ID = ID
		sefl.next_time = 0

	def sendOrder(exchange,time):
		self.order = self.order_queue.cancelOrder()
		self.exchange.receive_order(order,time)

	def readOrder(self):
		f = open("trader"+str(self.ID)+".csv" , "r")
		for line in f:
			temp_order = creatOrder(line)
			self.order_queue.putOrder(temp_order)
		f.close()
	def isEmpty():
		return order_queue.isEmpty()


class Exchange:
	"""docstring for Exchange"""
	def __init__(self, ID):
		self.order_queue = OrderQueue()
		self.ID = ID

	def receiveOrder(order,time):
		order.timestamp = time
		self.order_queue.putOrder(order)

	def sendOrder():
		pass

	def isEmpty():
		return order_queue.isEmpty()
		
class OrderQueue(list):
	"""docstring for Queue"""
	def __init__(self):
		#super(type(OrderQueue), self).__init__(not_full)
		#self.not_full = _threading.Condition(self.mutex)
		self.head_order = Order()
		#self.next_time = 0

	def putOrder(self,order):
		self.put(order)

	def cancelOrder():
		return sefl.get()
		
	def isEmpty():
		return empty()
		
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

	def simulate(self):
		traderToExchange()
		exchangeToOutput()

	def traderToExchange():
		while trader1.isEmpty() == False and trader2.isEmpty() == False:
			if trader1.order_queue.next_time < trader2.order_queue.next_time:
				time = self.time + trader1.order_queue.next_time
				trader1.sendOrder(exchange1,time)
			else :
				time = time + trader2.order_queue.next_time
				trader2.sendOrder(exchange1,time)
		if trader1.isEmpty():
			while trader2.isEmpty() == False:
				time = time + trader2.order_queue.next_time
				trader2.sendOrder(exchange1)
		else :
			while trader1.isEmpty() == False:
				time = time + trader1.order_queue.next_time
				trader2.sendOrder(exchange1)

	def exchangeToOutput():
		f = open ("output.csv" , "w")
		while exchange1.isEmpty() == False:
			head_order = exchange1.order_queue.cancelOrder()
			f.write(str(head_order.ID)+","+str(head_order.time)+","+str(head_order.timestamp)+"\n")
		f.close()

m = Market()
m.start()
m.simulate()
		
		



