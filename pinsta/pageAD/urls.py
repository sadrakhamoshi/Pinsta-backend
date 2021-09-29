from django.urls import path
from .viewsets import *

urlpatterns = [
    path('explore', page_ad_get),
    path('', page_ad_create),
    path('my_pages', page_ad_mine),
    path('<int:pk>', page_ad_detail),
    path('page_up_to_now', page_ad_up_to_now),
    path('search', page_ad_search),
    path('request', request_page_ad),
    path('request/reject/<int:pk>', request_page_ad_reject),
    path('request/accept/<int:pk>', request_page_ad_accept),
    path('favorite/add', page_ad_add_favorite),
    path('favorite/<int:pk>', page_ad_delete_favorite),
    path('favorite/my', page_ad_my_favorites),
]
