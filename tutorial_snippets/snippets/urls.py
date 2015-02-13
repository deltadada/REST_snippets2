from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    #url(r'^snippet/$', views.home),
    # url preceeds with snippets/

    url(r'^$', views.snippet_list),
    url(r'^(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^home/$', views.home),
]

#allows for url http://127.0.0.1:8000/snippets/.json
urlpatterns = format_suffix_patterns(urlpatterns)