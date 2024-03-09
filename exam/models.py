from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class ExamName(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ExamName, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    answer_type_options = (
        (1, 'Text'),
        (2, 'options'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(ExamName, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    answer_type = models.IntegerField(choices=answer_type_options, default=1)
    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    text_answer = models.CharField(max_length=100, blank=True, null=True)
    correct_option = models.CharField(max_length=100, blank=True, null=True)
    marks = models.IntegerField(default=1)
    negative_marks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.ForeignKey(ExamName, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam_name.name} - {self.percentage}%"