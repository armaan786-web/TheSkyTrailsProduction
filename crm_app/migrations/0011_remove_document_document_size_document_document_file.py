# Generated by Django 4.2.5 on 2023-10-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0010_alter_assignroles_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document_size',
        ),
        migrations.AddField(
            model_name='document',
            name='document_file',
            field=models.FileField(blank=True, null=True, upload_to='media/Documents'),
        ),
    ]
