# Generated by Django 3.2 on 2021-04-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_answers_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
