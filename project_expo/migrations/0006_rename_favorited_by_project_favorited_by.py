# Generated by Django 3.2.4 on 2021-06-15 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_expo', '0005_alter_project_favorited_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='favorited_By',
            new_name='favorited_by',
        ),
    ]
