from django.db import models
from genres.models import Genre
from actors.models import Actors


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField()
    actors = models.ManyToManyField(Actors, related_name='Movies')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
