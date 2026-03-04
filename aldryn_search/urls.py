from django.urls import re_path

from aldryn_search.views import AldrynSearchView


urlpatterns = [
    re_path('^$', AldrynSearchView.as_view(), name='aldryn-search'),
]
