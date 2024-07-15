from django.db import models
from django.urls import reverse

class Stars(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    condition = models.FloatField()
    profession = models.ForeignKey('Profession', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_star', kwargs={'star_id': self.pk})


class Profession(models.Model):
    profession = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.profession