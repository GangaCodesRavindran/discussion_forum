from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

def index(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect authenticated users to home page
    return render(request, 'login/index.html')

def logout(request):
    django_logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'login/home.html')

@login_required
def forum_redirect(request):
    return redirect('forum')  # Redirect to the forum API view

@login_required
def videos_redirect(request):
    return redirect('videos')  # Redirect to the videos view
