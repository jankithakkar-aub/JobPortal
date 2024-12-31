from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages

#index function to call index.html
def index(request):
    """View to show index.html"""
    return render(request, "index.html")

#signup function to call signup.html
def signup(request):
    """View to signup a user"""
    
    #SignUp form method is Post
    if request.method == "POST":

        #Creating a new user and check the user details via post method
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #Save the user to the database
            login(request, user)
            messages.success(request, "Account created successfully!")
            
            #Redirect the user to login page after successfully signup
            return redirect("login") 
        else:
            messages.error(request, "Error in form submission. Please try again!!")
    else:
        initial_data = {"username": "", "password1": "", "password2": ""} #to clear the fields when user is not registered
        form = UserCreationForm(initial=initial_data) #creating an empty form for GET request
    
    return render(request, "signup.html", {"form": form})


def login_user(request):
    """View to login a user"""

    #Login form method is Post
    if request.method == "POST":

        #Authenticating the new user and 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #Get the authenticated user from form
            login(request, user) #Log the user in
            messages.success(request, "User authorized successfully!")
            
            #Redirect the user to dashboard page after successfully login
            return redirect("dashboard") 
        else:
            messages.error(request, "Error in form submission. Please try again!!")
    else:
        initial_data = {"username": "", "password": ""} #to clear the fields
        form = AuthenticationForm(initial=initial_data) 
    
    return render(request, "login.html", {"form": form})

def logout_user(request):
    """View to logout a user"""
    logout(request)
    return redirect("login")

