# Generated by Django 4.0.2 on 2023-10-12 07:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0028_visacategory_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visasubcategory',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
