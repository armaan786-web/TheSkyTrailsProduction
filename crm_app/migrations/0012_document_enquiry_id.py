# Generated by Django 4.2.5 on 2023-10-05 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0011_remove_document_document_size_document_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='enquiry_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.enquiry'),
        ),
    ]