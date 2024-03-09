from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Category

# Create your views here.
def index(request):
    # category = Category.objects.all() # Перемещаем в пользовательский тэг
    context = {
        'title': 'Главная страница',
        'content': 'Магазин антиквариата',
        # 'category': category
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О магазине',
        'content': 'Краткая информация о магазине',
        'text_on_page': 'Информация о том какой магазин классный'
    }
    return render(request, 'main/about.html', context)
