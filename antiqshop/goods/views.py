from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Category, Products
from goods.utils import q_search


# Create your views here.

def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'goods':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    # doods = Products.objects.all()
    context = {
        'title': 'Главная страница',
        'goods': current_page,
        'slug_url': category_slug,
        # 'category': Category.objects.all()
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    # product = Products.objects.get(id=product_id)
    product = get_object_or_404(Products, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
