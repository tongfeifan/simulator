import Exchange

delay_time = 3


class Trader():
    """docstring for trader"""

    def __init__(self, trader_id, strategy_id, exchange):
        self.trader_id = trader_id
        self.strategy_ID = strategy_id
        self.order_queue = []
        self.exchange = exchange
        self.time = 0

    def generate_strategy(self):
        for x in xrange(1, 10):
            order_book = Exchange.OrderBook()
            order_book = self.exchange.get_oder_book(self.time)
            print(order_book)

    def operate_strategy(self):
        self.exchange.receive_order(self.order_queue, delay_time)

    def receiver_announcement(self):
        pass

    def set_strategy(self):
        pass


