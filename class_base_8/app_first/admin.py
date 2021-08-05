from django.contrib import admin
from .models import Comment, Todo

# Register your models here.
# admin.site.register(Todo)

# @admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created','puplished','slug')
    list_filter = ('puplished',)
    list_editable = ('puplished',)
    search_fields = ('title',)    
    prepopulated_fields = {'slug':('title',)}    
    
admin.site.register(Todo,TodoAdmin)

class CommetAdmin(admin.ModelAdmin):
    list_display = ('name','body')

admin.site.register(Comment,CommetAdmin)