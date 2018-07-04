from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.views import View 
#-----for google ==>>
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home

urlpatterns = [
url(r'^$',home.as_view()),
url(r'submitted/$',submitted.as_view()),
url(r'signup/$',signup.as_view()),
url(r'login_data/$',login_data.as_view()),
url(r'login/$',login.as_view()),

url(r'update/$',update.as_view()),
url(r'display_users/$',display_users.as_view()),
url(r'edit/$',edit.as_view()),
url(r'update/$',update.as_view()),
url(r'delete/(?P<id>\d+)$',delete.as_view()),
url(r'edit/(?P<id>\d+)$',edit.as_view()),
url(r'update/(?P<id>\d+)$',update.as_view()),
url(r'edit/(?P<id>\d+)$',update.as_view()),
url(r'login_data/(?P<id>\d+)$',login_data.as_view()),
url(r'send_otp/$',send_otp.as_view()),
url(r'reset_pass/$',reset_pass.as_view()),
url(r'check_OTP/$',check_OTP.as_view()),
url(r'update_pass/(?P<id>\d+)$',update_pass.as_view()),
url(r'^admin/', admin.site.urls),
url(r'^login/$', views.login, name='login'),
url(r'^logout/$', views.logout, name='logout'),
url(r'^auth/', include('social_django.urls', namespace='social')),  
url(r'^$', home, name='home'),


]