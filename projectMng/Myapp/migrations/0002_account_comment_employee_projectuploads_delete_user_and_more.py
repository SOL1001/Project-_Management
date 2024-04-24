# Generated by Django 4.2.7 on 2023-12-09 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('accounttype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
                ('commentText', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('researcherName', models.CharField(max_length=20)),
                ('researchTitle', models.CharField(max_length=20)),
                ('areaOfStudy', models.CharField(max_length=20)),
                ('yearOfStudy', models.IntegerField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField()),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Myapp.employee')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='account',
            name='Employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Myapp.employee'),
        ),
    ]
