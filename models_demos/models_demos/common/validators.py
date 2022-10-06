'''
How validators work:

- if valid - do nothing
- if invalid - raise ValidationError
'''
from datetime import date

from django.core.exceptions import ValidationError


def validate_in_the_past(value):
    if date.today() < value:
        raise ValidationError(f'{value} is in the future')
