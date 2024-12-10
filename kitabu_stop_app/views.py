import json
from urllib.request import HTTPBasicAuthHandler
from django.http import HttpResponse
from django.shortcuts import render, redirect
from kitabu_stop_app.models import User,Product,Contact, Resource
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from kitabu_stop_app.credentials import MpesaAccessToken, LipanaMpesaPpassword
import requests
from requests.auth import HTTPBasicAuth
from decimal import Decimal
from django.shortcuts import get_object_or_404
from .forms import ResourceForm


def index(request):
    if request.method=='POST': 
        if User.objects.filter(
            username = request.POST['username'],
            password = request.POST['password'],
        ).exists():
            return render(request, 'index.html')
        
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
    

def contact(request):
    if request.method=='POST':
        communication = Contact(
         name = request.POST['name'],
         email = request.POST['email'],
         message = request.POST['message']
    )
        communication.save()
        redirect('/confirmation')
        
    else:
        return render(request, 'contact.html')
    
    
    
    return render(request, 'contact.html')

def confirmation(request):
    return render(request, 'contact_confirmation.html')

def test(request):
    return render(request, 'test.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('login')

def shop(request):
    products = Product.objects.all()
    return render(request, 'book_store.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method=='POST':
        members= User(
            name = request.POST['name'],
            username = request.POST['username'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        members.save()
        print("success")
        return redirect('/login')
    
    else:
        return render(request, 'register.html')
        

def working(request):
    return render(request, 'working.html')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def search(request):
    if request.method == "POST":
        searched_term = request.POST.get('searched')  # Get the search term from the form
        
        if not searched_term:  # If the search term is empty
            messages.error(request, "Please enter a search term.")
            return render(request, "search.html")
        
        # Query the Products database model for products matching the search term (case-insensitive)
        products = Product.objects.filter(Q(name__icontains=searched_term) | Q(description__icontains=searched_term))
        
        # If no products match the search, show a message
        if not products:
            messages.error(request, "No products found matching your search.")
        
        return render(request, "search.html", {'searched': products, 'term': searched_term})

    # For GET request, render the search page without results
    return render(request, "search.html")

#mpesa API views

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuthHandler(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


def pay(request):
    return render(request, 'pay.html')
    # if request.method == 'POST':
    #     selected_product = get_object_or_404(Product, id=request.POST['selected_product'])
        
    #     details = payment_details(
    #         user=request.user, 
    #         phone=request.POST['phone'],
    #         selected_product=selected_product,
    #         amount=Decimal(request.POST['amount']),
    #     )
    #     try:
            
    #         details.save()
        
    #     except Exception as e:
    #         print(f"Error saving payment: {e}")

    #     return redirect('payment_success')

    # else:
    #     products = Product.objects.all()
    #     return render(request, 'pay.html', {'products': products})


# def pay(request):
#     if request.method == 'POST':
#         # Save payment details to the database
#         details = payment_details(
#             user = request.user,
#             phone = request.POST['phone'],
#             selected_product = Product.objects.get(id=request.POST['selected_product']),
#             amount = request.POST['amount'],
            
    
#         )
#         details.save()
#         print(request.POST)
        
        

#         # Redirect to a success page (use a named URL or a view function here)
#         return redirect('payment_success')  # This will redirect to a URL defined with 'payment_success'

#     else:
#         # Fetch products from the database to display in the dropdown
#         products = Product.objects.all()
#         print("fail")
#         # Render the 'pay.html' page, passing the products context
#         return render(request, 'pay.html', {'products': products})

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "ShemTechnologies",
            "TransactionDesc": "Service Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return redirect('payment')
    
def payment(request):
        return render(request, 'payment_success.html')
    
    
def resources(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})

    
    
def upload_resources(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resources')  # Redirect to resources after upload
    else:
        form = ResourceForm()

    return render(request, 'upload_resources.html', {'form': form})

    

def edit(request, id):
    resources = Resource.objects.get(id=id)
    return render(request, 'edit.html', {'x': resources})

        
    





