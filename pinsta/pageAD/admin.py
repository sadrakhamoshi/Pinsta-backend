from django.contrib import admin
from . import models

admin.site.register(models.PageAD)
admin.site.register(models.FavoritePage)
admin.site.register(models.PageAdRequest)
admin.site.register(models.Category)

