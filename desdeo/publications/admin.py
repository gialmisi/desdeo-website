from django.contrib import admin

from .models import Publication, OtherPublication

admin.site.register(Publication)
admin.site.register(OtherPublication)
