from django.shortcuts import render
from .utils import perform_ocr

def home(request):
    # a = perform_ocr("sample.pdf")
    context = {
        'all_exams':1,
        # 'a':a
    }
    return render(request, 'dashboard/home.html', context)