from django.shortcuts import render


def index(request):
    return render(request, "getinvolved/index.html", {})
