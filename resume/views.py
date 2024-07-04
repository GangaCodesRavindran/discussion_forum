from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume
import PyPDF2
import os
from django.core.files.storage import FileSystemStorage
from docx import Document
from docx.opc.exceptions import PackageNotFoundError
import pypandoc
import tempfile

@login_required
def upload_resume(request):
    skills = []
    error_message = None
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            file_path = resume.file.path
            try:
                if file_path.endswith('.pdf'):
                    skills = extract_skills_from_pdf(file_path)
                elif file_path.endswith('.docx'):
                    skills = extract_skills_from_docx(file_path)
                elif file_path.endswith('.doc'):
                    skills = extract_skills_from_doc(file_path)
                else:
                    error_message = "Unsupported file type. Please upload a PDF, DOC, or DOCX file."
            except Exception as e:
                error_message = f"Error processing file: {str(e)}"
    else:
        form = ResumeForm()
    return render(request, 'resume/upload_resume.html', {'form': form, 'skills': skills, 'error_message': error_message})

def extract_skills_from_pdf(file_path):
    skills = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    skill_keywords_path = os.path.join(os.path.dirname(__file__), 'skill_keywords.txt')
    with open(skill_keywords_path, 'r') as keywords_file:
        skill_keywords = [line.strip() for line in keywords_file.readlines()]

    for keyword in skill_keywords:
        if keyword.lower() in text.lower():
            skills.append(keyword)

    return skills

def extract_skills_from_docx(file_path):
    skills = []
    try:
        doc = Document(file_path)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
    except PackageNotFoundError:
        raise Exception("The uploaded file is not a valid DOCX file or is corrupted.")

    skill_keywords_path = os.path.join(os.path.dirname(__file__), 'skill_keywords.txt')
    with open(skill_keywords_path, 'r') as keywords_file:
        skill_keywords = [line.strip() for line in keywords_file.readlines()]

    for keyword in skill_keywords:
        if keyword.lower() in text.lower():
            skills.append(keyword)

    return skills

def extract_skills_from_doc(file_path):
    skills = []
    try:
        text = pypandoc.convert_file(file_path, 'plain')
    except Exception:
        raise Exception("The uploaded file is not a valid DOC file or is corrupted.")

    skill_keywords_path = os.path.join(os.path.dirname(__file__), 'skill_keywords.txt')
    with open(skill_keywords_path, 'r') as keywords_file:
        skill_keywords = [line.strip() for line in keywords_file.readlines()]

    for keyword in skill_keywords:
        if keyword.lower() in text.lower():
            skills.append(keyword)

    return skills
