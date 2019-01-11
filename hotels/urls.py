from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from hotels import views as core_views
from django.views.generic.base import TemplateView

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.auth import authenticate , login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from hotels.forms import SignUpForm

from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [
   ###path('signup',views.elmas,name='signup'),


    url(r'^$', TemplateView.as_view(template_name='main_page.html'), name='seda'),
   # url(r'^login/$', views.login, name='login'),
   ## url(r'^logout/$', views.logout, name='logout'),
    ##url(r'^logout/$', LogoutView,  name='logout', kwargs={'next_page': '/'}),
    url( r'^login/$', LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^hotel/new/$', views.new_hotel, name='hotel_new'),
   # url(r'^logout/$', views.logout, {'template_name': 'logged_out.html'}, name='logout'),

    url(r'^logout/$', views.logout, {'template_name': 'logged_out.html'}, name='logout'),

   #url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.elmas, name='signup'),
    path('main',views.seda,name='main_page'),
    #path('login',views.login,name='login'),
    path('check', views.check, name='check'),
    #url(r'^admin/', admin.site.urls),



]