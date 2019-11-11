from django.shortcuts import render

from .models import AboutDescription, TeamDescription, PublicationsDescription

# tuples of url names and display names
subpages_list = [
        ("about", "About"),
        ("software", "Software"),
        ("team", "Team"),
        ("news", "News"),
        ("blog", "Blog"),
        ("publications", "Publications"),
        ("getinvolved", "Get involved"),
    ]


def index(request):
    # pk=1 is safe for singleton models, it's the only entry
    featurettes = [
        AboutDescription.objects.get(pk=1),
        TeamDescription.objects.get(pk=1),
        PublicationsDescription.objects.get(pk=1),
    ]

    context = {
        "subpages_list": subpages_list,
        "featurettes": featurettes,
    }

    return render(request, "frontpage/index.html", context)
