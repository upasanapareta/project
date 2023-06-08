from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from .models import *
from django.contrib.auth.hashers import make_password,check_password


def index(request):
    if request.method == 'POST':
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id  = request.session.get('cart')
        # print("cart_id ----->",cart_id)
        if cart_id:
            quantity = cart_id.get(product_id )
            if quantity:
                    if remove:
                        if quantity <=1:
                            cart_id.pop(product_id)
                        else:
                            cart_id[product_id] = quantity - 1
                    else:
                        cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1
            
        request.session['cart'] = cart_id

    fetch_cat = Category.objects.all()
    
    cat_id = request.GET.get('category_id')
    search = request.GET.get('search')

    if cat_id:
        product = Product.objects.filter(pro_category=cat_id)
    elif search:
        product = Product.objects.filter(pro_name__icontains=search)
    else:
        product = Product.objects.all()
    context = {
        'cats':fetch_cat,
        'product':product
    }
    return render(request,'index.html',context=context)

def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        
        
        save_info = SignUp(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            gender=gender,
            mobile=mobile
        )
        save_info.save()
        return HttpResponse('registration successful')
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('emailid')
        password = request.POST.get('password')
        try:
            email_id = SignUp.objects.get(email=email)
            if email_id:
                if check_password(password,email_id.password):
                    request.session['name'] = email_id.first_name
                    request.session['customer_id'] = email_id.id
                    return redirect('home')
                else:
                    return HttpResponse('invalid credentials')
        except:
            return HttpResponse('Email does not exists')
        
        
def logout(request):
    request.session.clear()
    return redirect('home')


def cart_details(request):
    error = True
    if error and request.session.get('cart'):
        ids = list(request.session.get('cart').keys())
        product = Product.objects.filter(id__in=ids)
        
        return render(request, 'cart.html',{'cart_details': product})
    else:
        error = "No product found in cart"
        return render(request, 'cart.html',{error: error})


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse('please Login')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))
        for item in product:
            save_ord_dtls = Order(
                address =address,
                mobile = mobile,
                customer = SignUp(id=customer_id),
                product = item,
                quantity = cart.get(str(item.id)),
                price = item.pro_price
            )
            save_ord_dtls.save()
        request.session['cart'] = {}
        return redirect('order')
    
    
def order(request):
    # order_details = Order.objects.all()
    customer_id = request.session.get('customer_id')
    
    order_details = Order.objects.filter(customer=customer_id)
    
    tp = 0
    for item in order_details:
        tp += item.quantity * item.price
    return render(request, 'orders.html',{'order_details': order_details,'tp':tp})

from rest_framework import  viewsets
from .serializer import  SignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
