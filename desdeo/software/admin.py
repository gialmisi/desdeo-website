from django.contrib import admin

from .models import Content, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ImageAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, ]


admin.site.register(Content, ImageAdmin)
