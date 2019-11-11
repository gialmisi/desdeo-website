from django.shortcuts import render

from .models import Bio
from frontpage.views import subpages_list


def index(request):
    bios_list = Bio.objects.all()
    context = {
        "bios_list": bios_list,
    }
    print(subpages_list)
    return render(request, "biographies/index.html", context)
