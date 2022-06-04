# Generated by Django 4.0.5 on 2022-06-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=200)),
                ('is_done', models.BooleanField()),
                ('is_archive', models.BooleanField(default=False, help_text='Is this ToDo archived?')),
            ],
        ),
        migrations.AlterField(
            model_name='timer',
            name='short_link',
            field=models.CharField(blank=True, default='', help_text='timer short link (optional)', max_length=15),
        ),
        migrations.AddField(
            model_name='timer',
            name='todo',
            field=models.ManyToManyField(related_name='todo', to='api_v1.todo'),
        ),
    ]