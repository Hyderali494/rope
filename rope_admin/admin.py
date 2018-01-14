# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from models import Products
import bulk_admin

# Register your models here.

@admin.register(Products)
class ProAdmin(bulk_admin.BulkModelAdmin):
    search_fields = ('sku_code',)
    list_display = ('sku_code', 'title', 'image')
