from django.urls  import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from accounts.views import login
from accounts.views import register
from . import views

urlpatterns = [
    path('result', views.result, name='result'),
    path('accounts/login', login),
    path('accounts/register', register),
    url(r'^download/(?P<path>.*)$', serve,{'document root':settings.MEDIA_ROOT}),
]