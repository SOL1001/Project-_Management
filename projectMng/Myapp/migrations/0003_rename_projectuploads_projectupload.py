# Generated by Django 4.2.7 on 2023-12-09 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_account_comment_employee_projectuploads_delete_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectUploads',
            new_name='ProjectUpload',
        ),
    ]
