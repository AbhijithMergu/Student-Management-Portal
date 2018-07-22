# Generated by Django 2.0.5 on 2018-06-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=64)),
                ('acronym', models.CharField(max_length=8)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MockTest1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem1', models.IntegerField()),
                ('problem2', models.IntegerField()),
                ('problem3', models.IntegerField()),
                ('problem4', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('db_folder', models.CharField(max_length=50)),
                ('dropped_out', models.BooleanField(default=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.College')),
            ],
        ),
        migrations.AddField(
            model_name='mocktest1',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.Student'),
        ),
    ]
