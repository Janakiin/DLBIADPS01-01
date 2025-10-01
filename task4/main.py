from order_manager import OrderManager

orderManager = OrderManager()
orderManager.add_order("1",17.90)
orderManager.add_order("2",28.30)
orderManager.add_order("3",2.99)

result = orderManager.total_order_value()
print(f"{result:.2f}")
