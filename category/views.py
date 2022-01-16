from django.shortcuts import render, HttpResponse
from .models import Category, Subcategory, Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required()
def dashboard(request):
    context = {
        'posts': {}
    }
    return render(request, 'dashboard.html', context)


@login_required()
def category(request):
    sub_cat_id = request.GET.get('cat_id')
    product_list = Product.objects.filter(sub_category=sub_cat_id)

    paginator = Paginator(product_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print(page_obj[0].__dict__)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'sub-category.html', context)


def about(request):
    context = {
        'posts': {}
    }
    return render(request, 'about-us.html', context)


def contact(request):
    context = {
        'posts': {}
    }
    return render(request, 'contact-us.html', context)


def faq(request):
    context = {
        'posts': {}
    }
    return render(request, 'faq.html', context)
