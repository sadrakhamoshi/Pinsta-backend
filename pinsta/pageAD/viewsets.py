from .views import *

page_ad_get = PageADViewSet.as_view({
    'get': 'list',
})

page_ad_create = PageADViewSet.as_view({
    'post': 'create',
})

page_ad_detail = PageADViewSet.as_view({
    'put': 'update',
    'delete': 'destroy',
})

page_ad_mine = PageADViewSet.as_view({
    'get': 'get_my_page',
})

page_ad_search = PageADViewSet.as_view({
    'get': 'search',
})

page_ad_up_to_now = PageADViewSet.as_view({
    'get': 'get_page_up_to_now',
})

request_page_ad = PageAdRequestViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

request_page_ad_reject = PageAdRequestViewSet.as_view({
    'delete': 'destroy',
})

request_page_ad_accept = PageAdRequestViewSet.as_view({
    'delete': 'accept',
})

page_ad_add_favorite = FavoritePagesViewSet.as_view({
    'post': 'create'
})
page_ad_delete_favorite = FavoritePagesViewSet.as_view({
    'delete': 'destroy',
})

page_ad_my_favorites = FavoritePagesViewSet.as_view({
    'get': 'get_my_favorite'
})
