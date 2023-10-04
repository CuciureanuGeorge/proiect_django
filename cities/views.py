from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from cities.models import City, Country


def index(request):
    all_cities = City.objects.all()
    all_country = Country.objects.all()
    template = loader.get_template("index_city.html")
    context = {
        "cities": all_cities,
        "countries": all_country,
    }
    return HttpResponse(template.render(context, request))

