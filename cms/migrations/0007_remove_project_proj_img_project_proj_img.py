# Generated by Django 4.0 on 2024-02-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_remove_project_proj_img_project_proj_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='proj_img',
        ),
        migrations.AddField(
            model_name='project',
            name='proj_img',
            field=models.ManyToManyField(to='cms.ProjectImage'),
        ),
    ]