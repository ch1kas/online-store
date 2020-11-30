from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initializing a cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, id, product, quantity=1, update_quantity=False):
        """
        Adding product to cart.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'prod_id': id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):

        # cart session refreshing
        self.session[settings.CART_SESSION_ID] = self.cart
        # save session as modified to make sure
        self.session.modified = True

    def remove(self, product):
        """
        Deleting product from a cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iteration of products in the cart and retrieval of data from db.
        """
        product_ids = self.cart.keys()
        # adding products to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            # print(product)
            self.cart[str(product.id)]['product'] = product.title
            # print(self.cart)

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counting all the products in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Counting total cost.
        """
        return sum(float(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # deleting session from a cart
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True