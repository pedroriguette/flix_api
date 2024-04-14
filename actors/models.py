from django.db import models

nationality_choices = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil')
)


class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=nationality_choices,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
