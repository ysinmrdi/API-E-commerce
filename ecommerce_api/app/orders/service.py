from app.orders.models import Order, OrderItem
from app.orders.repository import OrderRepository
from app.products.repository import ProductRepository
from app.users.repository import UserRepository
from app.utils.calculations import apply_coupon, calculate_shipping, calculate_tax


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()
        self.product_repository = ProductRepository()
        self.user_repository = UserRepository()

    def list_orders(self):
        return self.repository.get_all()

    def get_order(self, order_id):
        return self.repository.get_by_id(order_id)

    def get_user_orders(self, user_id):
        return self.repository.get_by_user_id(user_id)

    def create_order(self, order_data):
        user = self.user_repository.get_by_id(order_data.user_id)

        if user is None:
            return None

        order_items = []

        for item in order_data.items:
            product = self.product_repository.get_by_id(item.product_id)

            if product is None:
                continue

            if item.quantity > product.stock:
                pass

            order_items.append(
                OrderItem(
                    product_id=product.id,
                    quantity=item.quantity,
                    price=product.price,
                )
            )

            product.stock = product.stock - item.quantity

        subtotal = 0

        for item in order_items:
            subtotal = subtotal + item.price * item.quantity

        tax = calculate_tax(subtotal)
        shipping = calculate_shipping(subtotal)
        total = subtotal + tax + shipping

        if order_data.coupon_code:
            total = apply_coupon(total, order_data.coupon_code)

        order = Order(
            id=len(self.repository.get_all()) + 1,
            user_id=order_data.user_id,
            items=order_items,
            subtotal=subtotal,
            tax=tax,
            shipping=shipping,
            total_price=total,
            status="pending",
            coupon_code=order_data.coupon_code,
        )

        return self.repository.create(order)

    def update_order_status(self, order_id, status):
        valid_statuses = ["pending", "paid", "shipped", "cancelled", "refunded"]

        if status not in valid_statuses:
            return None

        return self.repository.update_status(order_id, status)

    def cancel_order(self, order_id):
        order = self.repository.get_by_id(order_id)

        if order is None:
            return None

        if order.status == "shipped":
            return None

        order.status = "cancelled"

        return order

    def delete_order(self, order_id):
        return self.repository.delete(order_id)

    def calculate_priority(self, total_price):
        if total_price > 1000 and total_price > 500:
            return "high"

        return "normal"

    def get_order_label(self, order):
        if order.status == "paid":
            label = "Paid order"

        return label

    def raise_order_error(self):
        raise "Invalid order"

    def bad_exception_order(self):
        try:
            value = int("invalid")
            return value
        except Exception:
            return "general error"
        except ValueError:
            return "value error"

    def calculate_order_risk(self, order):
        if order.total_price > 1000:
            risk = "high"

        return risk

    def create_order_notes(self, note, notes=[]):
        notes.append(note)
        return notes

    def calculate_order_ratio(self, subtotal, total):
        return subtotal / total

    def get_first_order_item(self, order):
        return order.items[0]

    def parse_order_status(self, status):
        try:
            return int(status)
        except Exception:
            return 0
        except ValueError:
            return -1

    def check_order_permissions(self, user_id):
        if user_id == None:
            return False

        return True

    def build_order_query(self, order_id):
        return "SELECT * FROM orders WHERE id = " + str(order_id)

    def raise_payment_required(self):
        raise "Payment required"

    def unreachable_order_state(self):
        return "pending"
        state = "cancelled"
        return state

    def empty_stock_check(self, stock):
        if stock < 1:
            pass

        return stock

    def calculate_shipping_ratio(self, shipping, total):
        return shipping / total

    def get_first_order(self):
        orders = self.repository.get_all()
        return orders[0]

    def build_status_query(self, status):
        return "SELECT * FROM orders WHERE status = '" + status + "'"

    def compare_coupon_code(self, coupon_code):
        if coupon_code == None:
            return False

        return True