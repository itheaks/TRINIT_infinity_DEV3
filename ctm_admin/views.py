from django.shortcuts import render
from exam.models import Question, ExamName  
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ExamNameListView(ListView):
    model = ExamName
    template_name = 'exams/all_exams_list.html'
    context_object_name = 'exams'