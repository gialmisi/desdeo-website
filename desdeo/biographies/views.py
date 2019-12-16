from django.shortcuts import render

from .models import Bio, OtherContributor
from frontpage.views import subpages_list


def index(request):
    bios_list = Bio.objects.order_by("surname").order_by("order").all()
    others_list = OtherContributor.objects.order_by("surname").all()

    context = {
        "bios_list": bios_list,
        "others_list": others_list,
        "subpages_list": subpages_list,
        "this_page": "team",
    }

    return render(request, "biographies/index.html", context)
