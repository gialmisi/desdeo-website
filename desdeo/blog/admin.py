from django.contrib import admin

from .models import BlogContent, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ImageAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, ]


admin.site.register(BlogContent, ImageAdmin)
