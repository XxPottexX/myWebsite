from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from DanielG.models.customer import Customer
from django.views import View
from DanielG.models.product import Products
from DanielG.models.orders import Order
from DanielG.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        """The get method is used to render the order page according to the user that is logged in

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: Renders orders.html
        """
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
