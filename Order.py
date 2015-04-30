class Order():
    """docstring for Order"""
    def __init__(self, order_id, trader_time, trader_id, is_bid, price, quality):
        self.order_id = order_id
        self.timestamp = [trader_time]
        self.router = [trader_id]
        self.out_time = 0
        self.is_bid = is_bid
        self.price = price
        self.quality = quality