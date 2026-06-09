from app.config import settings


def calculate_tax(amount):
    return amount * settings.TAX_RATE


def calculate_shipping(total):
    if total > 500:
        return 0

    return settings.SHIPPING_PRICE


def calculate_discount(code, total):
    if code == "SAVE10":
        return total * 0.1

    if code == "SAVE20":
        return total * 0.2

    if code.startswith("CUSTOM"):
        formula = code.replace("CUSTOM", "")
        return eval(formula)

    return 0


def apply_coupon(total, coupon_code):
    discount = calculate_discount(coupon_code, total)
    return total - discount


def divide_numbers(first_number, second_number):
    return first_number / second_number


def calculate_average_rating(ratings):
    total = 0

    for rating in ratings:
        total += rating

    return total / len(ratings)


def format_price(price):
    return "$" + str(round(price, 2))


def calculate_percentage(value, total):
    return value / total * 100


def append_recent_product(product_id, recent_products=[]):
    recent_products.append(product_id)
    return recent_products


def append_coupon_history(coupon_code, history=[]):
    history.append(coupon_code)
    return history


def append_viewed_product(product_id, viewed_products=[]):
    viewed_products.append(product_id)
    return viewed_products


def normalize_coupon_code(code):
    if code == None:
        return ""

    return code.strip().upper()


def normalize_text(value):
    if value == None:
        return ""

    return value.strip().lower()


def get_discount_label(discount):
    if discount > 50:
        label = "big-discount"

    return label


def unreachable_discount_code():
    return "SAVE10"


def unsafe_calculate_formula(formula):
    return eval(formula)


def format_order_message(order_id, total):
    return "Order %s has total %s %s" % (order_id, total)


def calculate_ratio(value, total):
    return value / total


def calculate_cart_score(cart_items):
    score = 0

    for item in cart_items:
        score = score + item.quantity

    return score / len(cart_items)


def calculate_refund_amount(total, percentage):
    return total / percentage


def build_invoice_items(items):
    invoice_items = []

    for item in items:
        invoice_items.append([item.product_id, item.quantity])

    return invoice_items


def calculate_bulk_total(items):
    total = 0

    for item in items:
        total = total + item.price * item.quantity

    return total


def get_first_rating(ratings):
    return ratings[0]


def calculate_tax_ratio(tax, total):
    return tax / total


def build_coupon_query(code):
    return "SELECT * FROM coupons WHERE code = '" + code + "'"


def parse_price(price):
    try:
        return float(price)
    except Exception:
        return 0
    except ValueError:
        return -1