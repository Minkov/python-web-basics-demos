from django import template

register = template.Library()


def only_with_condition(numbers, condition_func):
    return [x for x in numbers if condition_func(x)]


@register.filter
def only_odd(numbers):
    return only_with_condition(numbers, lambda x: x % 2 > 0)


@register.filter
def only_even(numbers):
    return only_with_condition(numbers, lambda x: x % 2 == 0)


@register.filter
def only_positive(numbers):
    return only_with_condition(numbers, lambda x: x > 0)


@register.filter
def only_negative(numbers):
    return only_with_condition(numbers, lambda x: x < 0)

# def only_odd(numbers):
#     return [x for x in numbers if x % 2 > 0]

# def only_even(numbers):
#     return [x for x in numbers if x % 2 == 0]
