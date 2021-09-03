from django.db import models


class PageAD(models.Model):
    username_insta = models.CharField(max_length=250, null=False, blank=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    deadline = models.DateTimeField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    icon_url = models.ImageField(upload_to='pages/pictures/', null=True, blank=True)
    category = models.CharField(max_length=250, blank=True)
    sub_category = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'pages'
