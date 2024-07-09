# login\views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def learning_vid(request):
    return render(request, 'learning_vid/videos.html')

# @login_required
# def about(request):
#     return render(request, 'learning_vid/about.html')


# @login_required
# def contact(request):
#     return render(request, 'learning_vid/contact.html')

