# Generated by Django 3.2.4 on 2021-06-17 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish',
        ),
    ]
