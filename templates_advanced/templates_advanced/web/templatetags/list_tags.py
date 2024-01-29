import datetime

from django import template
from django.template.defaultfilters import safe

register = template.Library()


# Expects to return an HTML string to visualize
@register.simple_tag
def list_of(values):
    items_string = ''.join(f'<li>{value}</li>' for value in values)
    return safe(f'<ul>{items_string}</ul>')


@register.simple_tag
def current_time():
    return datetime.datetime.now()

# Expects to return an HTML string based on a template
# @register.inclusion_tag


# Expects to return a template Node with `render` func
# @register.tag
