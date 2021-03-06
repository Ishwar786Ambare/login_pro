from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html',)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form=AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form':form})




# def login(request):
#     username = "not logged in"
#
#     if request.method == "POST":
#         # Get the posted form
#         MyLoginForm = LoginForm(request.POST)
#
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#     else:
#         MyLoginForm = Loginform()
#
#     return render(request, 'loggedin.html', {"username": username})
