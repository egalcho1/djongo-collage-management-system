# Generated by Django 4.1 on 2022-09-15 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_student_block_student_depa_student_dorm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.IntegerField()),
                ('depa', models.CharField(max_length=255, null=True)),
                ('fild', models.CharField(max_length=255, null=True)),
                ('exp', models.CharField(max_length=255, null=True)),
                ('age', models.DateField(null=True)),
                ('dat', models.DateTimeField(auto_now_add=True)),
                ('salary', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='departiment',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('ccode', models.CharField(max_length=255, unique=True)),
                ('crdt', models.IntegerField()),
                ('ects', models.IntegerField()),
                ('adby', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('depart', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.departiment')),
            ],
        ),
    ]
