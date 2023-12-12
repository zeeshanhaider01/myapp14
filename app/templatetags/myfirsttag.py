from django import template
register=template.Library()

@register.filter
def my_filter(value,arg):
    return value+arg
    
@register.simple_tag
def my_tag(arg):
    return arg