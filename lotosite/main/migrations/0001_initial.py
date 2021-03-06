# Generated by Django 4.0.5 on 2022-06-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('anons', models.CharField(max_length=100, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Новина')),
                ('date', models.DateTimeField(verbose_name='Дата Публікації')),
            ],
            options={
                'verbose_name': 'Новини',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]
