import Trader
import Exchange

trader_ID = 1
strategy_ID = 1
exchange_ID = 1

exchange1 = Exchange.Exchange(exchange_ID)
trader1 = Trader.Trader(trader_ID, strategy_ID, exchange1)

exchange1.create_exchange(1)
# exchange1.print_exchange()
order_book = exchange1.get_oder_book(1)
for i in xrange(len(order_book.ask_list)):
    print("ask:"+order_book.ask_list[i])
for i in xrange(len(order_book.bid_list)):
    print("bid:"+order_book.bid_list[i])