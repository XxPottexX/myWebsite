from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from DanielG.models.customer import Customer
from django.views import  View
from DanielG.models.product import Products

class Cart(View):
    def get(self , request):
        """The get method gets the cart object and renders the cart template

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: Renders cart.html template
        """
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

