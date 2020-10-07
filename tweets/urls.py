from django.urls import path 

from . import views 

from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.home_view, name="home"),
]