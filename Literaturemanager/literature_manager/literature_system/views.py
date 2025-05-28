from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import UserRegistrationForm, BookForm
from django.contrib.auth import get_user_model  # Use the custom User model

# Get the custom User model
User = get_user_model()

# Home screen view
@login_required(login_url='login')
def home_screen_view(request):
    print(request.headers)
    return render(request, "home.html", {})

# Book data screen view
def book_data_screen_view(request):
    print(request.headers)
    return render(request, "book_data.html", {'books': Book.objects.all()})

# User registration view
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('home')  # Redirect after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Add new book - only accessible by librarian
def add_book(request):

    #if request.user.user_type != 'librarian':  Check if the user is a librarian
    #   return redirect('book_data')   Redirect if not a librarian

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_data')  # Redirect to book data after adding the book
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'title': 'Add New Book'})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting to authenticate user: {username}")
        user = authenticate(username=username, password=password)

        if user is not None:
            print(f"User authenticated: {user.username}")
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            print("Authentication failed.")
            messages.error(request, "Invalid username or password.")  # Error message on failure
    return render(request, 'login.html')

#Profile View
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

#Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
