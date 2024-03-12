from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import uploadform
from users.forms import UserCheckForm
from django.db.models import Q
from django.views.generic import ( 
    DetailView,
    
)
from django.db import IntegrityError

# Create your views here.
def index(request):
    products = Products.objects.order_by('-id')
    context = {'products' : products}
    return render(request, 'core/index.html', context)


def search(request):
    if request.method == 'GET':
        searched = request.GET.get("query")
        if searched:
            items = Products.objects.filter(Q(product_name__icontains=searched)| Q(price__icontains=searched))
            return render(request, 'core/searchpanel.html', {'items': items })
        else:
            print("NO information to Show")
            return render(request, 'core/searchpanel.html')
        
def upload_product(request):
    if request.method == 'POST':
        form = uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= uploadform()
    return render(request, 'core/upload.html',{'form': form})

        
def store(request):
    return render(request, 'core/store.html')


def checkout(request):
    check_form = UserCheckForm()
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals = []
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity
        item_totals.append(item_total)
        total_price += item_total
    item_with_total = zip(cart_items, item_totals)
    return render(request, 'core/checkout.html', {'item_with_total' : item_with_total, 'total_price' : total_price, "check_form":check_form})


def product(request):
    return render(request, 'core/product.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals = []
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity
        item_totals.append(item_total)
        total_price += item_total
    item_with_total = zip(cart_items, item_totals)
    return render(request, 'core/cart.html', {'total_price': total_price, 'item_with_total': item_with_total})

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart_item= CartItem.objects.get(product=product, user=request.user)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        try:
            cart_item=CartItem.objects.create(product=product, user=request.user, quantity=1)
        except IntegrityError as e:

            print(f"IntegerityError {e}")
  
    return redirect('cart')

def increase_cart_quantity(request, pk):
    product = get_object_or_404(Products, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity +=1
        cart_item.save()
    else:
        pass
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')

def subtract_from_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, user=request.user)
    cart_item.quantity -= 1
    if cart_item.quantity <=0:
        cart_item.delete()
    else:
        cart_item.save()

    return redirect('cart')


    


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'core/product.html'
