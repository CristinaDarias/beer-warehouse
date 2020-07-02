# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import CommonInfo


def image_upload_location(instance, filename):
    return 'media/beer/images/%s.png' % instance.id


# Create your models here.
class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)

    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BROWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (COLOR_YELLOW, 'yellow'),
        (COLOR_AMBER, 'amber'),
        (COLOR_BROWN, 'brown'),
        (COLOR_BLACK, 'black'),
    )

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    is_filtered = models.BooleanField('Is filtered?', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey('Company', related_name="beers", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['name']

    def __str__(self):
        return self.name

    def has_more_alcoholic_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = "Special ingredient"
        verbose_name_plural = "Special ingredients"
        ordering = ['name']

    def __str__(self):
        return self.name
