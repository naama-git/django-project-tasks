from urllib import request
from django.contrib import admin
from .models import  Task, Team


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
  
    fields = ('title', 'description', 'team','due_date')
    readonly_fields=('status','assigned_employee','assigned_employee' )
    list_filter = ('status', 'team','assigned_employee')
    search_fields = ('title', 'status','due_date','assigned_employee__user__username')


    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return False
        return obj.assigned_employee is None

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.assigned_employee is None


admin.site.register(Team)