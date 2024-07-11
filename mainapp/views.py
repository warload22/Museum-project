import os
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Exhibits, ExhibitsCategories

# Create your views here.

MODULE_DIR = os.path.dirname(__file__)


def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)

    return json.load(open(file_path, encoding='utf-8'))


def index(request):
    content = {
        'title': 'Музей АГЗ МЧС РФ'
    }

    return render(request, 'mainapp/index.html', content)


def products(request, id_category=None, page=1):

    if id_category:
        products_ = Exhibits.objects.filter(category_id=id_category)
    else:
        products_ = Exhibits.objects.all()

    pagination = Paginator(products_, per_page=6)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)

    content = {
        'title': 'Geegshop - Каталог',
        'categories': ExhibitsCategories.objects.all(),
        'products': product_pagination
    }

    return render(request, 'mainapp/products.html', content)

class ProductDetail(DetailView):
    model = Exhibits
    template_name = 'mainapp/detail.html'