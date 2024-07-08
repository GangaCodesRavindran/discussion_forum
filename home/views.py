from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

@login_required
def home(request):
    return render(request, 'home/home.html')

@login_required
def about(request):
    return render(request, 'home/about.html')


@login_required
def contact(request):
    return render(request, 'home/contact.html')

class ProfileView(View):
    def get(self, request):
        return render(request, 'home/profiles.html')
