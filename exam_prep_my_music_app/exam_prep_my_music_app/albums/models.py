from django.core.validators import MinValueValidator
from django.db import models

from exam_prep_my_music_app.profiles.models import Profile

"""
- Owner
    - This field should remain hidden in forms.
"""


class Genre(models.TextChoices):
    GENRE_POP = "Pop Music"
    GENRE_JAZZ = "Jazz Music"
    GENRE_ROCK = "Rock Music"
    GENRE_COUNTRY = "Country Music"
    GENRE_RNB = "R&B Music"
    GENRE_DANCE = "Dance Music"
    GENRE_HIP_HOP = "Hip Hop Music"
    GENRE_OTHER = "Other"


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MIN_PRICE = 0.0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name",
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist",
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=Genre.choices,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
