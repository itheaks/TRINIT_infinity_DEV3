from django import forms
from .models import Question, ExamName

class ExamForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'marks', 'negative_marks']

class ExamNameForm(forms.ModelForm):
    class Meta:
        model = ExamName
        fields = ['name']