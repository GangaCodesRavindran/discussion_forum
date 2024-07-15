# disc_forum\views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

class ForumView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Welcome to the discussion forum!"})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('forum')
    else:
        form = QuestionForm()
    return render(request, 'disc_forum/post_question.html', {'form': form})

@login_required
def delete_question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('forum')
    return render(request, 'disc_forum/confirm_delete.html', {'object': question, 'type': 'question'})

@login_required
def update_question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_detail', pk=pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'disc_forum/update_question.html', {'form': form, 'question': question})


from django.shortcuts import render
from .models import Question
from .forms import QuestionForm, AttachmentForm


def forum(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        attachment_form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid() and attachment_form.is_valid():
            question = form.save()
            attachment = attachment_form.save(commit=False)
            attachment.question = question
            attachment.save()
    else:
        form = QuestionForm()
        attachment_form = AttachmentForm()

    questions = Question.objects.all()
    context = {
        'form': form,
        'attachment_form': attachment_form,
        'questions': questions,
    }
    return render(request, 'disc_forum/forum.html', context)

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'disc_forum/question_detail.html', {'question': question, 'form': form})

@login_required
def delete_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    question_pk = answer.question.pk
    if request.method == 'POST':
        answer.delete()
        return redirect('question_detail', pk=question_pk)
    return render(request, 'disc_forum/confirm_delete.html', {'object': answer, 'type': 'answer'})

@login_required
def update_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    question_pk = answer.question.pk
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('question_detail', pk=question_pk)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'disc_forum/update_answer.html', {'form': form, 'answer': answer})
