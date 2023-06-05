"""
URL configuration for hyperjob_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from vacancy.views import IndexView, MySignupView, MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
    path('', include('vacancy.urls')),
    path('', IndexView.as_view(), name="index"),
    path('signup', MySignupView.as_view(), name="signup"),
    path('login', MyLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]
