
from django.contrib import admin
from django.urls import path
from TasksApp.views import home, tasksListView, update_task_member, update_task_status,logout_view
from TasksApp.views import register
from TasksApp.views import login_view



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('tasks/', tasksListView, name='tasksList'),
    path('update-task/<int:task_id>/', update_task_status, name='update_task_status'),
    path('update-task-member/<int:task_id>/', update_task_member, name='update_task_member'),
    path('logout/', logout_view, name='logout'),
    
]



