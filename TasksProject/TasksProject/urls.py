
from django.contrib import admin
from django.urls import path
from TasksApp.views import home
from TasksApp.views import register
from TasksApp.views import login_view
from TasksApp.views import logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
