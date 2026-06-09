from app.database import products_db
from app.products.models import Product


class ProductRepository:
    def get_all(self):
        return products_db

    def get_by_id(self, product_id):
        for product in products_db:
            if product.id == product_id:
                return product
        return None

    def search(self, query):
        result = []

        for product in products_db:
            if query.lower() in product.name.lower() or query.lower() in product.description.lower():
                result.append(product)

        return result

    def get_by_category(self, category):
        result = []

        for product in products_db:
            if product.category == category:
                result.append(product)

        return result

    def create(self, product_data):
        product = Product(
            id=len(products_db) + 1,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock=product_data.stock,
            category=product_data.category,
        )

        products_db.append(product)

        return product

    def update(self, product_id, product_data):
        product = self.get_by_id(product_id)

        if product is None:
            return None

        update_data = product_data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product, key, value)

        return product

    def delete(self, product_id):
        product = self.get_by_id(product_id)

        if product is None:
            return False

        products_db.remove(product)

        return True

    def remove_out_of_stock_products(self):
        for product in products_db:
            if product.stock == 0:
                products_db.remove(product)

        return products_db

    def build_product_query(self, search_text):
        query = "SELECT * FROM products WHERE name LIKE '%" + search_text + "%'"
        return query

    def get_product_name(self, product_id):
        product = self.get_by_id(product_id)

        if product:
            name = product.name

        return name

    def create_search_history(self, keyword, history=[]):
        history.append(keyword)
        return history

    def calculate_stock_percentage(self, stock, total_stock):
        return stock / total_stock * 100

    def get_first_product(self):
        return products_db[0]

    def remove_products_by_category(self, category):
        for product in products_db:
            if product.category == category:
                products_db.remove(product)

        return products_db

    def compare_category(self, category):
        if category == None:
            return False

        return True

    def build_admin_product_query(self, category, minimum_price):
        return "SELECT * FROM products WHERE category='" + category + "' AND price > " + str(minimum_price)

    def empty_product_validation(self, product):
        if product.price < 0:
            pass

        return product

    def unreachable_product_code(self):
        return products_db
        product_count = len(products_db)
        return product_count

    def calculate_product_score(self, price, stock):
        return price / stock

    def build_delete_query(self, product_id):
        return "DELETE FROM products WHERE id = " + str(product_id)

    def append_product_cache(self, product_id, cache=[]):
        cache.append(product_id)
        return cache

    def calculate_price_ratio(self, price, original_price):
        return price / original_price