from django.contrib import admin
from .models import Task
# Register your models here.

# admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'completed', 'created',)
    list_filter = ('title', 'completed',)
    list_editable = ('completed',)
    search_fields = ('title', 'completed')
    raw_id_fields = ()
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Task, TaskAdmin)