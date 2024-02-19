from django.core.exceptions import ValidationError


def validate_username(username):
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
