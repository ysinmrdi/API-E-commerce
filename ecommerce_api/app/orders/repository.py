from app.database import orders_db


class OrderRepository:
    def get_all(self):
        return orders_db

    def get_by_id(self, order_id):
        for order in orders_db:
            if order.id == order_id:
                return order
        return None

    def get_by_user_id(self, user_id):
        result = []

        for order in orders_db:
            if order.user_id == user_id:
                result.append(order)

        return result

    def create(self, order):
        orders_db.append(order)
        return order

    def update_status(self, order_id, status):
        order = self.get_by_id(order_id)

        if order is None:
            return None

        order.status = status

        return order

    def delete(self, order_id):
        order = self.get_by_id(order_id)

        if order is None:
            return False

        orders_db.remove(order)

        return True