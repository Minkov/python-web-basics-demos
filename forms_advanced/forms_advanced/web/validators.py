'''
Django wants a callable with a single arg that raise a ValidationError if data is invalid
'''

from django.core.exceptions import ValidationError


def validate_email(email):
    if "@" not in email:
        raise ValidationError("Email is invalid")


class FileSizeValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f"The size of the file should be less that {self.max_file_size} ")


validate_email("doncho@minkov.com")
# FileSizeValidator(5)(file)
