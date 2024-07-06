import sweetify
from django import template
register = template.Library()
@register.simple_tag(name='success_message')
def success_message(request,message):
    return sweetify.success(request, message)