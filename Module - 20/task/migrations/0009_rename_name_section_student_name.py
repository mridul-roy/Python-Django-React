# Generated by Django 5.2 on 2025-04-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_rename_student_section_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='name',
            new_name='student_name',
        ),
    ]
