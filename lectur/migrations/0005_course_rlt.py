# Generated by Django 4.1 on 2022-09-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectur', '0004_course_lectur'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rlt',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
