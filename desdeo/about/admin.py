from django.contrib import admin

from .models import Content, Image, Downloadable, Video


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Content, ImageAdmin)
admin.site.register(Downloadable)
admin.site.register(Video)
