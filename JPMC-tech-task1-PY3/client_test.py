import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
	def test_getDataPoint_calculatePrice(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			bid_price = quote['top_bid']['price']
			ask_price = quote['top_ask']['price']
			price = (ask_price + bid_price) / 2
			self.assertEqual(getDataPoint(quote), (quote['stock'], bid_price, ask_price, price))

	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		quotes = [
			{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			bid_price = quote['top_bid']['price']
			ask_price = quote['top_ask']['price']
			price = (ask_price + bid_price) / 2
			self.assertEqual(getDataPoint(quote), (quote['stock'], bid_price, ask_price, price))


	""" ------------ Add more unit tests ------------ """
	def test_getRatioZeroB(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		prices = dict()
		for quote in quotes:
			bid_price = quote['top_bid']['price']
			ask_price = quote['top_ask']['price']
			price = (ask_price + bid_price) / 2
			prices[quote['stock']] = price
		#print("When stock-B is zero, prices are", prices)
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), None)

	def test_getRatioZeroA(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'},
			{'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'ABC'}
		]
		prices = dict()
		for quote in quotes:
			bid_price = quote['top_bid']['price']
			ask_price = quote['top_ask']['price']
			price = (ask_price + bid_price) / 2
			prices[quote['stock']] = price
		#print("When stock-A is zero, prices are ", prices)
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), 0)

	def test_getRatio(self):
		quotes = [
			{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		prices = dict()
		for quote in quotes:
			bid_price = quote['top_bid']['price']
			ask_price = quote['top_ask']['price']
			price = (ask_price + bid_price) / 2
			prices[quote['stock']] = price
		#print("When stock prices are non-zero, prices are", prices)
		self.assertEqual(getRatio(prices['ABC'], prices['DEF']), 1.0005426841995408)



if __name__ == '__main__':
		unittest.main()
