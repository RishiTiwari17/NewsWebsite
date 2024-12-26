"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include('webapp.urls')),
    path('' , views.index , name='home'),
    path('cat/' , views.Category , name='cat'),
    path('info/' , views.SearchBar, name='info'),
    path('login/' , views.Login, name='login'),
    path('signup/' , views.signup, name='signup'),
    path('logout/' , views.Logout  ,name='logout'),
    path('accounts/' , include('allauth.urls')),
    path('subscription/' , views.subsription , name='subscribe'),
    path('payment/<str:amount>' , views.payment , name='payment'),
    path('success/' , views.result , name='success'),
    path('failure/' , views.fail , name='failure')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns 