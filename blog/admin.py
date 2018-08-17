from django.contrib import admin
from . import models

admin.site.site_header = '博客管理后台'


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 30


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 30


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time', 'status']
    list_per_page = 30
    inlines = [CommentInline]
    readonly_fields = ['text']





