from app.products.repository import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def list_products(self):
        return self.repository.get_all()

    def get_product(self, product_id):
        return self.repository.get_by_id(product_id)

    def search_products(self, query):
        if query == "":
            return self.repository.get_all()

        return self.repository.search(query)

    def filter_by_category(self, category):
        return self.repository.get_by_category(category)

    def create_product(self, product_data):
        return self.repository.create(product_data)

    def update_product(self, product_id, product_data):
        return self.repository.update(product_id, product_data)

    def delete_product(self, product_id):
        return self.repository.delete(product_id)