# Generated by Django 4.1 on 2022-09-20 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectur',
            name='depa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lectur.departiment'),
        ),
    ]