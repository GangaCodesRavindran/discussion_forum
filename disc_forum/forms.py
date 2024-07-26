# disc_forum/forms.py
from django import forms
from .models import Question, Attachment, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['Keyword', 'Description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['Response', 'attachment']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']
