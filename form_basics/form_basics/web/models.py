from django.core.exceptions import ValidationError
from django.db import models


def non_empty_spaces(value):
    if " " in value:
        raise ValidationError(message='Spaces not allowed')


class Department(models.Model):
    name = models.CharField(max_length=25)


class Employee(models.Model):
    MAX_FIRST_NAME_LENGTH = 35
    ROLES = (
        (1, 'Software Developer'),
        (2, 'QA engineer'),
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,
        null=False,
        validators=(non_empty_spaces,)
    )

    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )

    role = models.IntegerField(
        choices=ROLES,
        blank=False,
        null=False,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
