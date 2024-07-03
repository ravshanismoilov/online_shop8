from django.shortcuts import render, redirect
from .models import Category, Products, Review
from django.views import View
from .forms import CreateProductForm


class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'index.html', context=context)


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'base.html', context=context)


class ProductView(View):
    def get(self, request, pk):
        products = Products.objects.filter(category=pk)
        context = {
            'products': products
        }
        return render(request, 'products/category_detail.html', context=context)


class ProductDetail(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)
        context = {
            'product': product
        }
        return render(request, 'products/product_detail.html', context=context)


class CreateProduct(View):
    def get(self, request):
        create_form = CreateProductForm()
        context = {
            'create_form': create_form
        }
        return render(request, 'products/create_product.html', context=context)

    def post(self, request):
        create_form = CreateProductForm(request.POST, request.FILES)
        if create_form.is_valid():
            product = create_form.save()
            return redirect('product-detail', pk=product.pk)
        context = {
            'create_form': create_form
        }
        return render(request, 'products/create_product.html', context=context)