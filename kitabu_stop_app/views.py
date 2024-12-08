from django.shortcuts import render, redirect
from kitabu_stop_app.models import user,Product,Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

def index(request):
    if request.method=='POST': 
        if user.objects.filter(
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

def resources(request):
    return render(request, 'resources.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method=='POST':
        members= user(
            name = request.POST['name'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        members.save()
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

        
    





