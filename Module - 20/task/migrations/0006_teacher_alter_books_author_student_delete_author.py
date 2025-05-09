# Generated by Django 5.2 on 2025-04-24 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_author_alter_books_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=20)),
                ('roll_number', models.CharField(max_length=20)),
                ('validity_status', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
