from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    """Use @register.filter() as a decorator.
       Determines if product is present in the cart

        :param product: First parameter that is a product object
        :param cart: Second parameter that is a cart object

        :returns: True if product id is found, else returns false

        :rtype: Boolean
    """
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    """Use @register.filter() as a decorator.
       Determines how many products are in the cart

        :param product: First parameter that is a product object
        :param cart: Second parameter that is a cart object

        :returns: Number of total items in the cart

        :rtype: int
    """
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0


@register.filter (name='price_total')
def price_total(product, cart):
    """Use @register.filter() as a decorator.
       Determines total price of the specific product

        :param product: First parameter that is a product object
        :param cart: Second parameter that is a cart object

        :returns: Total product price 

        :rtype: Float
    """
    return product.price * cart_quantity (product, cart)


@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    """Use @register.filter() as a decorator.
       Determines total order cost for all items
    
        :param product: First parameter that is a product object
        :param cart: Second parameter that is a cart object

        :returns: Total order cost

        :rtype: Float
    """
    sum = 0
    for p in products:
        sum += price_total (p, cart)

    return sum
