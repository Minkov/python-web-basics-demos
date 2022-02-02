from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    Capitalizes the value, i.e. makes the first letter capital and lowers the rest

    * THIS is TExt => This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()


@register.filter
def do_nothing(value):
    return value
