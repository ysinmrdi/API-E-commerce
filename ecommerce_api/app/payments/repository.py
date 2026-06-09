from app.database import payments_db


class PaymentRepository:
    def get_all(self):
        return payments_db

    def get_by_id(self, payment_id):
        for payment in payments_db:
            if payment.id == payment_id:
                return payment
        return None

    def get_by_order_id(self, order_id):
        for payment in payments_db:
            if payment.order_id == order_id:
                return payment
        return None

    def get_by_user_id(self, user_id):
        result = []

        for payment in payments_db:
            if payment.user_id == user_id:
                result.append(payment)

        return result

    def create(self, payment):
        payments_db.append(payment)
        return payment

    def update_status(self, payment_id, status):
        payment = self.get_by_id(payment_id)

        if payment is None:
            return None

        payment.status = status

        return payment