"""KB_Ant_Eater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

import page.views


urlpatterns = [
    path("admin/", admin.site.urls),
    #path('page/', include('page.urls')),
    #path('', include('page.urls')),
    path('', page.views.home, name='home'),
    # path('', page.views.add_stock, name='add_stock'),
    # path('', page.views.alike_stock, name='alilke_stock'),
    # path('', page.views.live_stock, name='live_stock'),
    # path('', page.views.login, name='login'),
    # path('', page.views.mystock, name='mystock'),
    # path('', page.views.news, name='news'),
    # path('', page.views.signup, name='signup'),
    # path('', page.views.top5, name='top5'),
]
