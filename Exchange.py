import random
import string
import time


def exchange_read_file(exchange, tick):
    if tick == 1:
        f = file("GE.CSV")
    f.readline()
    file_line = f.readline()
    for x in xrange(1, 300):
        tick_list = string.split(str(file_line.rstrip('\n')), ",")
        exchange.tick_table.append(tick_list)


class OrderBook():
    """This is a class of OrderBook"""

    def __init__(self):
        self.bid_list = []
        self.ask_list = []

    def matching(self, order):
        if order.is_bid == 0:
            # this is a bid order, maching with ask order
            if order.price >= self.ask_list[0][1]:
                return True
            else:
                return False
        else:
            # this is a ask order, maching with bid order
            if order.price <= self.bid_list[0][1]:
                return True
            else:
                return False

    def create(self, current_time, tick_table):
        self.__init__()
        for x in xrange(0, 299):
            if current_time > tick_table[x][9] and current_time < tick_table[x][10]:
                bid_quantity = tick_table[x][4]
                bid_price = tick_table[x][5]
                ask_quantity = tick_table[x][6]
                ask_price = tick_table[x][7]
                self.bid_list.append([bid_quantity, bid_price])
                self.ask_list.append([ask_quantity, ask_price])
        self.ask_list.sort()
        self.bid_list.sort()


class Exchange():
    """This is a class for Exchange"""

    def __init__(self, exchange_id):
        self.exchange_id = exchange_id
        self.order_book = OrderBook()
        self.tick_table = []
        self.result = []
        self.order_queue = []
        self.time = 0

    def create_exchange(self, tick=0):
        if tick == 0:
            tick = random.randint(1, 1)  # This is random function to decide which tick will be chosen
        exchange_read_file(self, tick)

    def resort_order_queue(self):
        self.order_queue.sort()

    def receive_order(self, order_queue, timestamp):
        self.order_queue.extend(order_queue)
        self.resort_order_queue()

    def create_order_book(self):
        self.order_book.create(self.time, self.tick_table)

    def print_exchange(self):
        i = 0
        for i in range(len(self.tick_table)):
            print self.tick_table[i]

    def trading(self):
        i = 0
        while self.order_queue[i]:
            order = self.order_queue[i]
            self.time = order.timestamp[-1] + order.outtime
            self.create_order_book()
            if order.out_time > 2000:
                new_result = [order.order_id, order.router[0], self.time, 0]
                self.result.append(new_result)
            elif self.order_book.matching(order):
                new_result = [order.order_id, order.router[0], self.time, 1]
                self.result.append(new_result)
            else:
                self.order_queue[i].outtime += 1
                self.resort_order_queue()

    def send_result(self):
        i = 0
        while self.result[i]:
            print self.result[i]
            i += 1

    def get_oder_book(self, current_time):
        self.order_book.create(current_time, self.tick_table)
        return self.order_book

