import re
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile, Skill
from .forms import ResumeUploadForm
from django.contrib.auth.decorators import login_required
from docx import Document
from PyPDF2 import PdfFileReader


def extract_skills_from_text(text):
    skills = re.findall(r'\b(Python|Java|Cordova|Docker|HTML|CSS|JavaScript)\b', text, re.IGNORECASE)
    return skills


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfFileReader(file)
        for page in range(reader.getNumPages()):
            text += reader.getPage(page).extract_text()
    return text


def extract_text_from_word(file_path):
    text = ""
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text
    return text


@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            file_path = form.instance.resume.path
            if file_path.endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            elif file_path.endswith('.docx'):
                text = extract_text_from_word(file_path)
            else:
                text = ""

            skills = extract_skills_from_text(text)
            for skill_name in skills:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                request.user.userprofile.skills.add(skill)

            return redirect('profile')
    else:
        form = ResumeUploadForm()
    return render(request, 'user_profiles/upload_resume.html', {'form': form})


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    skills = user_profile.skills.all()
    return render(request, 'user_profiles/profile.html', {'user_profile': user_profile, 'skills': skills})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

