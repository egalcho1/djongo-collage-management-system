# Generated by Django 4.1 on 2022-09-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]