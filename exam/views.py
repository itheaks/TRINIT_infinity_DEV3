from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, ExamName, Result
from .form import ExamForm, ExamNameForm
from django.contrib import messages

class ExamNameListView(ListView):
    model = ExamName
    template_name = 'exams/all_exams_list.html'
    context_object_name = 'exams'

class ExamNameCreateView(CreateView):
    model = ExamName
    form_class = ExamNameForm
    template_name = 'exam_name/create.html'
    success_url = reverse_lazy('exam_name_list')

class ExamNameUpdateView(UpdateView):
    model = ExamName
    form_class = ExamNameForm
    template_name = 'exam_name/update.html'
    success_url = reverse_lazy('exam_name_list')

class ExamNameDeleteView(DeleteView):
    model = ExamName
    template_name = 'exam_name/confirm_delete.html'
    success_url = reverse_lazy('exam_name_list')

class ExamListView(ListView):
    model = Question
    template_name = 'exams/exam_qa_list.html'
    context_object_name = 'questions'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam_slug = self.kwargs.get('slug')
        exam_instance = get_object_or_404(ExamName, slug=exam_slug)
        context['exam'] = exam_instance
        return context

class ExamDetailView(DetailView):
    model = Question
    template_name = 'exam/exam_detail.html'
    context_object_name = 'exam'

class ExamCreateView(CreateView):
    model = Question
    form_class = ExamForm
    template_name = 'exams/exam_form.html'
    
    def form_valid(self, form):
        exam_slug = self.kwargs.get('slug')
        exam_instance = get_object_or_404(ExamName, slug=exam_slug)
        form.instance.author = self.request.user
        form.instance.exam_name = exam_instance
        return super().form_valid(form)
    
class ExamUpdateView(UpdateView):
    model = Question
    form_class = ExamForm
    template_name = 'exam/exam_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ExamDeleteView(DeleteView):
    model = Question
    template_name = 'exam/exam_confirm_delete.html'
    success_url = '/'

def take_exam_view(request, slug):
    exam = get_object_or_404(ExamName, slug=slug)
    questions = Question.objects.filter(exam_name=exam)
    total_questions = questions.count()
    total_marks=0
    for question in questions:
        total_marks += question.marks
    context = {
        'course':exam,
        'total_questions':total_questions,
        'total_marks':total_marks
        }
    return render(request, 'exams/take_exam.html', context)

def start_exam_view(request, slug):
    if request.method == 'POST':
        if request.COOKIES.get('course_id') is None:
            return HttpResponse("Your exam has been expired. Please start again.")
        course_id = request.COOKIES.get('course_id')
        exam = get_object_or_404(ExamName, id=course_id)
        
        total_marks=0
        obtained_marks=0
        questions=Question.objects.all().filter(exam_name=exam)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            total_marks = total_marks + questions[i].marks
            if selected_ans == actual_answer:
                obtained_marks = obtained_marks + questions[i].marks
        result = Result(user=request.user, exam_name=exam, total_marks=total_marks, obtained_marks=obtained_marks)
        result.save()
        messages.success(request, f'Your exam has been submitted successfully. Your obtained marks is {obtained_marks} out of {total_marks}')
        return redirect('exam-view-result')
    exam = get_object_or_404(ExamName, slug=slug)
    questions = Question.objects.filter(exam_name=exam)
    context = {
        'course':exam,
        'questions':questions
    }
    response= render(request,'exams/start_exam.html',context)
    response.set_cookie('course_id',exam.id)
    return response

def view_result_view(request):
    results = Result.objects.filter(user=request.user)
    context = {
        'results':results
    }
    return render(request, 'exams/view_result.html', context)