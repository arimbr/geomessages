from django.conf.urls import url

from messageboard import views

urlpatterns = [
    url(r'messages/$', views.message_list),
]
