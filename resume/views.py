# # resume\views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ResumeForm
# from .models import Resume
# import PyPDF2
# from django.core.files.storage import FileSystemStorage


# @login_required
# def upload_resume(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.user = request.user
#             resume.save()
#             skills = extract_skills(resume.file.path)
#             # return render(request, 'resume/upload_success.html', {'skills': skills})
#             return redirect('profiles')

#     else:
#         form = ResumeForm()
#     return render(request, 'resume/upload_resume.html', {'form': form})

# def extract_skills(file_path):
#     skills = []
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         # for page_num in range(reader.numPages):
#         #     page = reader.getPage(page_num)
#         #     text += page.extractText()
#         for page in reader.pages:
#             text += page.extract_text()
    
#     # Simple skill extraction logic (you can improve this)
#     skill_keywords = ['Python', 'Django', 'JavaScript', 'HTML', 'CSS', 'Java', 'C++', 'SQL']
#     for keyword in skill_keywords:
#         if keyword.lower() in text.lower():
#             skills.append(keyword)
    
#     return skills


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume
import PyPDF2
import os
from django.core.files.storage import FileSystemStorage


@login_required
def upload_resume(request):
    skills = []
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            skills = extract_skills(resume.file.path)
            # return render(request, 'resume/upload_success.html', {'skills': skills})
            # return redirect('profiles')

    else:
        form = ResumeForm()
    return render(request, 'resume/upload_resume.html', {'form': form, 'skills': skills})

def extract_skills(file_path):
    skills = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Read skill keywords from a file
    skill_keywords_path = os.path.join(os.path.dirname(__file__), 'skill_keywords.txt')
    with open(skill_keywords_path, 'r') as keywords_file:
        skill_keywords = [line.strip() for line in keywords_file.readlines()]

    for keyword in skill_keywords:
        if keyword.lower() in text.lower():
            skills.append(keyword)

    return skills
