from django.shortcuts import render

from .models import Publication, OtherPublication
from frontpage.views import subpages_list

def index(request):
    publication_list = Publication.objects.order_by("-year")
    other_publication_list = OtherPublication.objects.order_by("-year")
    
    context = {
        "publication_list": publication_list,
        "other_publication_list": other_publication_list,
        "subpages_list": subpages_list,
        "this_page": "publications",
    }
    return render(request, "publications/index.html", context)
