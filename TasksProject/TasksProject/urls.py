
from django.contrib import admin
from django.urls import path
from TasksApp.views import register

from TasksApp.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
]
