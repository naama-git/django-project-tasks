from django.contrib import admin
from .models import  Task, Team


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
  
    fields = ('title', 'description', 'team','due_date')
    readonly_fields=('status','assigned_employee','assigned_employee' )
    search_fields = ('title', 'status','due_date','assigned_employee__username')
    list_filter = ('status', 'team','assigned_employee')


admin.site.register(Team)