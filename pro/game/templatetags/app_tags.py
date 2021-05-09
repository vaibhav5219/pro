from django import template
register=template.Library()

@register.filter
def mul(v1,v2):
    return v1*v2

@register.filter
def add(v1,v2):
    return v1+v2

@register.filter
def sub(v1,v2):
    return v1-v2

@register.filter
def div(v1,v2):
    return v1/v2


