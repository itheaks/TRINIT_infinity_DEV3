# Generated by Django 5.0.3 on 2024-03-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_rename_auther_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='examname',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]