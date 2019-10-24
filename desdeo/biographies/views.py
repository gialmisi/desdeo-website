from django.shortcuts import render

from .models import Bio


def index(request):
    bios_list = Bio.objects.all()
    context = {
        "bios_list": bios_list,
    }
    return render(request, "biographies/index.html", context)
