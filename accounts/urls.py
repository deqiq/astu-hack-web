from django.contrib import admin
from django.urls import path, include
from . import views

app_name="accounts"
urlpatterns = [
    path('myaccount', views.myaccount,  name='myaccount'),
    path('usertype', views.usertype,  name='usertype'),
    path('profile', views.profile,  name='profile'),
    path('auth', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),
    # path('register', views.register,name='register'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # # path('accounts/', include('accounts.urls')),
    # path('events/', include('events.urls')),
]