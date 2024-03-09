from django.urls import path
from .views import ExamListView, ExamDetailView, ExamCreateView, ExamUpdateView, ExamDeleteView, ExamNameListView, ExamNameCreateView, ExamNameUpdateView, ExamNameDeleteView
from .views import take_exam_view, start_exam_view, view_result_view

urlpatterns = [
    path('', ExamNameListView.as_view(), name='exams-all_list'),
    path('<slug>/', ExamListView.as_view(), name='exams-details'),
    path('<slug>/create/', ExamCreateView.as_view(), name='exams-questions-create'),

    path('<slug>/take-exam/', take_exam_view,name='exams-take-exam'),
    path('<slug>/start-exam/', start_exam_view,name='exams-start-exam'),
    path('view-result', view_result_view,name='exam-view-result'),

    path('<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('<int:pk>/update/', ExamUpdateView.as_view(), name='exam-update'),
    path('<int:pk>/delete/', ExamDeleteView.as_view(), name='exam-delete'),

    path('exam-names/create/', ExamNameCreateView.as_view(), name='exam_name_create'),
    path('exam-names/<int:pk>/update/', ExamNameUpdateView.as_view(), name='exam_name_update'),
    path('exam-names/<int:pk>/delete/', ExamNameDeleteView.as_view(), name='exam_name_delete'),
]