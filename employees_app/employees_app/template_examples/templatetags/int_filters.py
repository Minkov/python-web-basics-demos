from django import template

register = template.Library()


@register.filter
def increase_by(value, number):
    try:
        return value + number
    except TypeError:
        return int(value) + number
