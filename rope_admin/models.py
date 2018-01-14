# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Products(models.Model):
    sku_code = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, default='')
    image = models.FileField(upload_to='static/images/')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PRODUCT'
    
