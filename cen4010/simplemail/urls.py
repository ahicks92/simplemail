from django.conf.urls import patterns, url
from . import views

urlpatterns=patterns('',
    url(r'^get_all_mailgun_messages$', views.get_all_mailgun_messages, name='get_all_mailgun_messages'),
)
