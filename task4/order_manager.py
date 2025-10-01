class OrderManager:
    def __init__(self):
        self.orders = {}  # order_id -> order_value

    def add_order(self, order_id: str, order_value: float):
        if not isinstance(order_id, str) or order_id.strip() == "":
            raise ValueError("order_id muss ein nicht-leerer String sein.")

        if not isinstance(order_value, (int, float)):
            raise ValueError("order_value muss eine Zahl sein.")

        if order_value < 0:
            raise ValueError("Bestellwert darf nicht negativ sein.")

        if order_id in self.orders:
            raise KeyError(f"Bestellung mit ID {order_id} existiert bereits.")

        self.orders[order_id] = order_value

    def total_order_value(self) -> float:
        return sum(self.orders.values())