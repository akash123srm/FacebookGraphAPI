from django.conf.urls import patterns, url
from test_app import views


urlpatterns = patterns('',
     url(r'^$', views.AuthorizeView.as_view(), name='authorize_view'),
     url(r'^login', views.login_view, name='login_view'),
     url(r'^home$', views.HomeView.as_view(), name='home_view'),

)
