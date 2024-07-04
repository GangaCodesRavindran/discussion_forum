# login/views.py

from .models import Employee
from datetime import datetime
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

x = datetime.now()
y = x.strftime('%d-%m-%y')

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
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
    return render(request, 'login/index.html', {'form': form})

def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee_list')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "login/employee_list.html", context)

def employee_update(request, id):
    employee = Employee.objects.get(id=id)
    return redirect('/employee_list')

@login_required
def home(request):
    return render(request, 'login/home.html')

@login_required
def forum_redirect(request):
    return redirect('forum')

@login_required
def videos_redirect(request):
    return redirect('videos')
