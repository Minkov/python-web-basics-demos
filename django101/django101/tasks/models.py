from django.db import models


# Code-first approach
class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False,
    )
    text = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return f'{self.id}: {self.title}'


class Category(models.Model):
    name = models.CharField(
        max_length=20,
    )
