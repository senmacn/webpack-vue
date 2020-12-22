from django.contrib import admin
from .models import Article, Tag, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',
                    'created_time', 'modified_time', 'views')
    search_fields = ('first_name', 'last_name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)
