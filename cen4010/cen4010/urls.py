from django.conf.urls import patterns, include, url
from django.contrib import admin
import simplemail.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cen4010.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(simplemail.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name='login'),
)
