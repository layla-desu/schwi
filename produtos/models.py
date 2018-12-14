# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(object):

    def __init__(self, name='', value='', description=''):
        self.name = name,
        self.value = value,
        self.description = description
