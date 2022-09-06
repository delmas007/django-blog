from django.contrib import admin

from posts.models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_update', 'created_on', 'published')
    list_editable = ('published', )



