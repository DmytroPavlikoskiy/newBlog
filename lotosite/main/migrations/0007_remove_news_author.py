# Generated by Django 4.0.6 on 2022-07-07 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_news_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
