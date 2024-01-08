from django.contrib import admin
from .models import Post, Category, PostCategory, Author, Comment


class ClassInLine(admin.TabularInline):
    model = PostCategory
    extra = 1

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (ClassInLine,)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Comment)
# Register your models here.
