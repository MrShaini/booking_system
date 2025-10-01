from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("login")
        else:
            messages.error(request, "Данні введені некоректно!")
            return redirect("register")
    else:
        register_form = UserRegistrationForm()
        return render(request, "register.html", context={"register_form": register_form})
    
def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            usernbame = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=usernbame, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Користувача не зареєстровано!")
                return redirect("login")
        else:
            messages.error(request, "Данні введені некоректно!")
            return redirect("login")
    else:
        login_form = AuthenticationForm()
        return render(request, "login.html", context={"login_form": login_form})
    
def logout_view(request):
    logout(request)
    return redirect('login')