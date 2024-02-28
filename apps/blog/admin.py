from django.contrib import admin
from .models import Blog, Category, Tag, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")
    search_fields = ("title", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")
    search_fields = ("title", )



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "author", 'category', ]
    list_display_links = ['id', 'title', "author", ]
    search_fields = ['title']
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date', 'slug', "modified_date"]
    filter_horizontal = ('tags',)
    # autocomplete_fields = ('author',)
