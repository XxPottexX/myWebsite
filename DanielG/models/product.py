from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='static/assets/')

    @staticmethod
    def get_products_by_id(ids):
        """Returns product by id

            :param ids: id of product

            returns: Product corresponding with id
        """
        return Products.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_products():
        """Returns all products

            returns: All products
        """
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        """Returns all products of that category

            :param category_id: id of category

            returns: All products of that category
        """
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()