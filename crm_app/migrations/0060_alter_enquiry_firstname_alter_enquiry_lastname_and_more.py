# Generated by Django 4.2.5 on 2023-11-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0059_chatgroup_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='FirstName',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='LastName',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='MiddleName',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
