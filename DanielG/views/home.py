from django.shortcuts import render , redirect , HttpResponseRedirect
from DanielG.models.product import Products
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        """The post method is used to get the input from the user from the home page.
         This is choosing the product they want to buy, adding to cart or removing from cart.

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :retruns: Redirects to home page
        """
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('DanielG:homepage')



    def get(self , request):
        """The get method gets the product path

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.
        """
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    """The store function renders the index template that creates the product grid

        :param request: Required parameter to send HTTP requests.
    """
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


