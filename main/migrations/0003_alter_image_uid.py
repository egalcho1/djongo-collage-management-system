# Generated by Django 4.1 on 2022-08-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_image_us_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uid',
            field=models.IntegerField(null=True),
        ),
    ]
