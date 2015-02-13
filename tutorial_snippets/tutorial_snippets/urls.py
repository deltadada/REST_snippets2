from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'snippets.views.home', name='home'),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^admin/', include(admin.site.urls)),


)
