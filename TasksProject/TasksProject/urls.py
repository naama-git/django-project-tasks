
from django.contrib import admin
from django.urls import path
from TasksApp.views import home, tasksListView
from TasksApp.views import register
from TasksApp.views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('tasks/', tasksListView, name='tasksList'),
]
