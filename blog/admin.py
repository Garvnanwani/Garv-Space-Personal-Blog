from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("title/author/intro/publish/category/imageId/slug", {'fields': ["title", "author","intro","publish","category","imageId","slug"]}),
        ("content", {"fields": ["body"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Post, PostAdmin)
