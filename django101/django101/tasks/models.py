from django.db import models


# Maps to a DB Table
class Task(models.Model):
    # varchar(30) NOT NULL
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()

    priority = models.IntegerField()
