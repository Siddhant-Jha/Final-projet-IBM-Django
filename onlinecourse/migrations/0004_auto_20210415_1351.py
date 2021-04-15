# Generated by Django 3.1.7 on 2021-04-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20210415_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=240),
        ),
    ]
