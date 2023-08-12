from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from DanielG.models.customer import Customer
from django.views import View

from DanielG.models.product import Products
from DanielG.models.orders import Order


class CheckOut(View):
    def post(self, request):
        """The post method is where the user input for the checkout is fetched and creates order object.

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: Redirects to updated cart page
        """
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('DanielG:cart')
