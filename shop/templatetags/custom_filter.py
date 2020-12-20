from django import template
register=template.Library()


@register.filter(name='rupee')
def addRupeeSign(value):
    return f'₹ {value}'

@register.filter(name='sell_price')
def getSalePrice(product):
    return int(product.price - (product.price* (product.discount/100)))

@register.filter(name='percentage')
def addPercentage(value):
    return f'{value}%'