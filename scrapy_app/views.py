import datetime
from django.http import HttpResponse

from scrapy_app.models import Product


def hello_world(request):
    return HttpResponse("Hello world from django!")


def get_date(request):
    return HttpResponse("<html><body<<h1>" + str(datetime.datetime.now()) + "</h1></body><html>")


def path_variable(request, name, age):
    return HttpResponse("{} this is your age: {}".format(name, age))


def create_product(request, id, name):
    new_product = Product(id, name)
    new_product.save()
    return HttpResponse("OK")
