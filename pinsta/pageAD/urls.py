from django.urls import path
from .viewsets import *

urlpatterns = [
    path('explore', page_ad_get),
    path('', page_ad_create),
    path('my_pages', page_ad_mine),
    path('<int:pk>', page_ad_detail),
    path('search', page_ad_search),
    path('request', request_page_ad),
    path('request/reject/<int:pk>', request_page_ad_reject),
    path('request/accept/<int:pk>', request_page_ad_accept),
]
