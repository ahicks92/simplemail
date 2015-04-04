from django.conf.urls import patterns, url
from . import views

urlpatterns=patterns('',
    url(r'^get_all_mailgun_messages$', views.get_all_mailgun_messages, name='get_all_mailgun_messages'),
    url(r'^inbox$', views.inbox, name='inbox'),
    url(r'^view_message/(\d+)$', views.view_message, name='view_message'),
    url(r'^send_message', views.send_message, name='send_message'),
    url(r'^create_account', views.create_account, name='create_account'),
    url(r'^delete_message/(\d+)', views.delete_message, name ='delete_message'),
    url(r'^outbox', views.outbox, name='outbox'),
    url(r'^trash', views.trash, name='trash'),
)
