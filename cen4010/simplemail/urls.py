from django.conf.urls import patterns, url
from . import views

urlpatterns=patterns('',
    url(r'^get_all_mailgun_messages$', views.get_all_mailgun_messages, name='get_all_mailgun_messages'),
    url(r'^inbox$', views.inbox, name='inbox'),
    url(r'^view_message/(\d+)$', views.view_message, name='view_message'),
)
