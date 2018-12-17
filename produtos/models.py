# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    value = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    description = models.CharField(max_length=255, null=False)
