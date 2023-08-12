from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from DanielG.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        """The get methods renders the login page

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: renders login.html
        """
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        """The post method is where the login is processed and validated.
            In the html file POST is used to get the user input and validate it.

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: Redirects to home page if succesfully logged in, else if error in login details reset login page with error message
        """
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('DanielG:homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    """The logout method is used to logout the user when the user chooses to logout

        :param request: required parameter to send HTTP requests.

        :returns: Redirects back to login page
    """
    request.session.clear()
    return redirect('DanielG:login')
