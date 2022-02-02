from django.urls  import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from accounts.views import login
from accounts.views import register
from accounts.views import logout
from . import views
#from .views import generate_view

urlpatterns = [
    path('history', views.history, name='history'),
    url(r'^bloodsugarview/(?P<tstrs_id>\d)/$', views.bloodsugarview, name='bloodsugarview'),
    url(r'^cholesterolview/(?P<tstrs_id>\d)/$', views.cholesterolview, name='cholesterolview'),
    url(r'^urinalysisview/(?P<tstrs_id>\d)/$', views.urinalysisview, name='urinalysisview'),
    path('accounts/login', login),
    path('accounts/register', register),
    path('accounts/logout', logout),
    url(r'^download/(?P<path>.*)$', serve,{'document root':settings.MEDIA_ROOT}),
]

