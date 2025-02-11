from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    product_queryset = Product.objects.all()
    paginator = Paginator(product_queryset, 6)  # Show 6 products per page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, "falcon/product_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'falcon/product_detail.html', {'product': product})