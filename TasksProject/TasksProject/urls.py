
from django.contrib import admin
from django.urls import path

from TasksApp.views import home, register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('register/', register_view, name='register')
]
