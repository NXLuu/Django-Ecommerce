from itertools import product
from django.shortcuts import render, redirect
from shop.models import *
from manager.form import *
# Create your views here.
def all_product(request):
    products = Product.objects.filter(is_draft=False)
    context = {
        'products': products,
    }
    return render(request, 'manager/book-list.html', context)
def emp(request):  
    if request.method == "POST":  
        form = CreatePostForm(data=request.POST, files=request.FILES)  
        print(form.is_valid())
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/manager')  
            except:  
                pass  
    else:  
        form = CreatePostForm()  
    return render(request,'manager/book-form.html',{'form':form})  
def edit(request, id):  
    product = Product.objects.get(id=id) 
    form = CreatePostForm(instance = product)  
    return render(request,'manager/edit.html', {'product':product, 'form': form})  
def update(request, id):  
    product = Product.objects.get(id=id)  
    form = CreatePostForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/manager")  
    return render(request,'manager/edit.html', {'product':product, 'form': form})  
def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/manager")  
def add_product(request, product_id):
    product_details = Product.objects.get(id=product_id)
    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)
    context = {
        'product': product_details,
        'related_products': related_products
    }
    return render(request, 'shop/product-details.html', context)

def wishlist(request):
    return render(request, 'shop/wishlist.html')
