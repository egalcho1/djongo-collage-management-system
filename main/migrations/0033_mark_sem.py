# Generated by Django 4.1 on 2022-09-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_mark_fname_mark_lname_mark_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='sem',
            field=models.IntegerField(null=True),
        ),
    ]
