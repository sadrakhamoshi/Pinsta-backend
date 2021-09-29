from django.db import models


class PageAD(models.Model):
    owner = models.ForeignKey('account.User', on_delete=models.CASCADE, blank=True)

    # TODO
    username_insta = models.CharField(max_length=250, blank=True, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    # TODO validator
    deadline = models.DateTimeField(blank=True, null=True)

    # TODO validator
    rating = models.IntegerField(null=True, blank=True)
    icon_url = models.ImageField(upload_to='pages/pictures/', null=True, blank=True)

    # TODO make better
    category = models.CharField(max_length=250, blank=True)
    sub_category = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'pages'


class FavoritePage(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    page = models.ForeignKey('PageAD', on_delete=models.CASCADE)

    class Meta:
        db_table = 'favorite_pages'


class PageAdRequest(models.Model):
    WEEK = 'w'
    MONTH = 'm'
    YEAR = 'y'

    memberships = [
        (WEEK, 'WEEK'),
        (MONTH, 'MONTH'),
        (YEAR, 'YEAR'),
    ]

    page_ad = models.ForeignKey('pageAD', on_delete=models.CASCADE)
    membership = models.CharField(max_length=10, choices=memberships)

    class Meta:
        db_table = 'requests'
