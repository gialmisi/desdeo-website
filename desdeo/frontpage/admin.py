from django.contrib import admin

from .models import AboutDescription, TeamDescription, PublicationsDescription

admin.site.register(AboutDescription)
admin.site.register(TeamDescription)
admin.site.register(PublicationsDescription)
