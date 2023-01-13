from django.urls import path, re_path

from service.views import index, page, about, file_show, json_show

urlpatterns = [
    path("", index),
    re_path(r"^service/(?P<page_num>[0-9]{3})", page),
    path('about/<int:id>', about, name='about'),
    path('file', file_show, name='file'),
    path('json', json_show, name='json')
]
