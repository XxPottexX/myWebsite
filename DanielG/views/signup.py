from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from DanielG.models.customer import Customer
from django.views import View


class Signup (View):
    """This is the signup class that will contain the methods for registering"""

    def get(self, request):
        """The get method is used to render the signup html file

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.
        
            :returns: Renders signup.html
        """
        return render (request, 'signup.html')

    def post(self, request):
        """The post method is where the registration is processed and validated.
            In the html file POST is used to get the user input and validate it.

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: Redirects to home page if succesfully signed up, else if error reset signup page
        """
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('DanielG:homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        """The function is used to validate the input of the user and check if the user doesn't already exist

            :param self: First parameter to the Instance method. The instance is called onto itself with the request parameter.
            :param request: Second required parameter to send HTTP requests.

            :returns: error_message if validation catches an error

            :rtype: str
        """
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message