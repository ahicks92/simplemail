from django.conf.urls import patterns, url
from . import views
# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy

urlpatterns=patterns('',
    url(R'^$', views.inbox),
    url(r'^get_all_mailgun_messages$', views.get_all_mailgun_messages, name='get_all_mailgun_messages'),
    url(r'^inbox$', views.inbox, name='inbox'),
    url(r'^view_message/(\d+)$', views.view_message, name='view_message'),
    url(r'^send_message', views.send_message, name='send_message'),
    url(r'^create_account', views.create_account, name='create_account'),
    url(r'^delete_message/(\d+)', views.delete_message, name ='delete_message'),
    url(r'^outbox', views.outbox, name='outbox'),
    url(r'^trash', views.trash, name='trash'),
    url(r'^reply_to_message/(\d+)', views.reply_to_message, name = "reply_to_message"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {
            "next_page" : reverse_lazy('login')
          }, name="logout"),

    #Mailgun's url
    url(r'^incoming_message$', views.incoming_message_view),
)
