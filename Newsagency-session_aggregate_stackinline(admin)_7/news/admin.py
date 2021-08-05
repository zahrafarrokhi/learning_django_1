from django.contrib import admin
from .models import Article, Author, Category,Comment

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['number_of_comments', ]
    list_display = ('title', 'author', 'abstract_context')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'context')
        }),
        ('Detail', {
            'fields': ('seen_num', 'category'),
        }),

    )
    inlines = [CommentInline,]
    search_fields = ('title', 'context',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)

