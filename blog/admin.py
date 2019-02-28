from django.contrib import admin
from blog.models import Post, Comment
# Register your models here.


class AdminPost(admin.ModelAdmin):

    list_display = ('title', 'slug', 'publish', 'author',
                    'updated', 'created', 'status')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, AdminPost)


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name','created', 'comment', 'active', 'post')


admin.site.register(Comment, CommentAdmin)
