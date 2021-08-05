# Generated by Django 3.2.4 on 2021-08-04 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_first', '0003_auto_20210620_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tcomments', to='app_first.todo')),
            ],
        ),
    ]