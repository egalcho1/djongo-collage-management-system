# Generated by Django 4.1 on 2022-09-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectur', '0006_course_add_alter_course_adby'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectur',
            name='cid',
            field=models.IntegerField(null=True),
        ),
    ]