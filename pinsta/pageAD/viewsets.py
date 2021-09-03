from .views import PageADViewSet

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
