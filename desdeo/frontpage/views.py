from django.shortcuts import render


def index(request):
    subpages_list = [
        "about",
        "team",
        "news",
        "publications",
    ]
    context = {
        "subpages_list": subpages_list,
    }

    return render(request, "frontpage/index.html", context)
