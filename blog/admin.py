from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
                    'title',
                    'slug',
                    'created_on',
                    'image',
                    )

    search_fields = [
                     'title',
                     'body_text',
                    ]

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
