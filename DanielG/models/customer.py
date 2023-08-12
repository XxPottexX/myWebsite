from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        """Saves registered customer

            :param self: Parameter to the Instance method. The instance is called onto itself.
        """
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        """Identifies customer by email

        :param email:user email

        :returns: Customer object, else if not registered customer retrun false
        """
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        """Tests if customer exists

        :param self: Parameter to the Instance method. The instance is called onto itself.

        :returns: True if user exists, False if not

        :rtype: Boolean
        """
        if Customer.objects.filter(email = self.email):
            return True

        return False