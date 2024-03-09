# Generated by Django 5.0.3 on 2024-03-09 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_examname_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('obtained_marks', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.examname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
