from django.db import models

from core.models import CommonInfo


class Bar(CommonInfo):
    name = models.CharField('Name', max_length=200)

    class Meta:
        verbose_name = "Bar"
        verbose_name_plural = "Bars"
        ordering = ['name']

    def __str__(self):
        return self.name
