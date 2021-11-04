from django.shortcuts import render

from .models import MaterialEntry, MaterialFile
from frontpage.views import subpages_list


def index(request):
    material_list = MaterialEntry.objects.order_by("name")

    # fetch all files per material entry
    files_list = []
    for material in material_list:
        files = MaterialFile.objects.filter(material_entry_id=material.id)
        files_list.append(files)

    context = {
        "materials_files_list": list(zip(material_list, files_list)),
        "subpages_list": subpages_list,
        "this_page": "materials",
    }
    return render(request, "materials/index.html", context)
