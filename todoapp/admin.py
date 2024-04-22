from django.contrib import admin
from .models import Project, Todo

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_date', 'completion_status', 'project')
    list_filter = ('completion_status', 'project')
    search_fields = ('description', 'project__title')  
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Todo, TodoAdmin)
