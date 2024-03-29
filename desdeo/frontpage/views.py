from django.shortcuts import render

from .models import Featurette, CarouselImages

# tuples of url names and display names
subpages_list = [
    ("about", "About"),
    ("software", "Software"),
    ("team", "Team"),
    ("news", "News"),
    ("publications", "Publications"),
    ("getinvolved", "Get involved"),
    ("materials", "Materials"),
]


def index(request):
    # pk=1 is safe for singleton models, it's the only entry
    featurettes = Featurette.objects.order_by("order").all()

    carousel_images = CarouselImages.objects.order_by("order").all()

    context = {
        "subpages_list": subpages_list,
        "featurettes": featurettes,
        "carousel_images": carousel_images,
    }

    return render(request, "frontpage/index.html", context)
