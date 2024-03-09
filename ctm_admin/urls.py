from django.urls import path
from .views import *

urlpatterns = [
    path('', ExamNameListView.as_view(), name='exam_name_list'),
]