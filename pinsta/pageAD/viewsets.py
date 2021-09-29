from .views import PageADViewSet, PageAdRequestViewSet

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

request_page_ad_create = PageAdRequestViewSet.as_view({
    'post': 'create'
})

request_page_ad_list = PageAdRequestViewSet.as_view({
    'get': ' list'
})

request_page_ad_reject = PageAdRequestViewSet.as_view({
    'delete': 'destroy',
})

request_page_ad_accept = PageAdRequestViewSet.as_view({
    'delete': 'accept',
})
