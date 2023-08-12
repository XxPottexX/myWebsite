from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    """Use @register.filter() as a decorator.
       returns the price with currency   
    
        :param number: Price of product or items

        :returns: price with currency

        :rtype: str
    """
    return "R "+str(number)



@register.filter(name='multiply')
def multiply(number , number1):
    """Use @register.filter() as a decorator.
       Returns total price
    
        :param number: Price of product or items
        :param number1: Total number of items
        
        :returns: Total price

        :rtype: float
    """
    return number * number1

