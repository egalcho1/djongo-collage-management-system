# Generated by Django 4.1 on 2022-09-03 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_complent_cfrom_alter_complent_comfrom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complent',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
