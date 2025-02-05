from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from basket.models import Basket
from mainapp.models import Exhibits


# Create your views here.

# @login_required
# def basket_add(request, id):
#     user_select = request.user
#     product = Product.objects.get(id=id)
#     baskets = Basket.objects.filter(user=user_select, product=product)
#
#     if baskets:
#         basket = baskets.first()
#         basket.quantity +=1
#         basket.save()
#     else:
#         Basket.objects.create(user=user_select,product=product,quantity=1)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

@login_required
def basket_add(request, id):
    if is_ajax(request=request):
        user_select = request.user
        product = Exhibits.objects.get(id=id)
        baskets = Basket.objects.filter(user=user_select, product=product)

        if baskets:
            basket = baskets.first()
            basket.quantity +=1
            basket.save()
        else:
            Basket.objects.create(user=user_select,product=product,quantity=1)

        products = Exhibits.objects.all()
        context = {'products': products}

        result = render_to_string('mainapp/includes/card.html', context)
        return JsonResponse({'result': result})

@login_required
def basket_remove(request,basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_edit(request,basket_id,quantity):
    if is_ajax(request=request):
        basket = Basket.objects.get(id=basket_id)
        if quantity > 0:
                basket.quantity = quantity
                basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user = request.user)
        context = {'baskets': baskets}

        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result':result})