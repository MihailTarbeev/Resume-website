# Generated by Django 4.2.5 on 2023-09-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_info_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=550, verbose_name='Контент')),
                ('sort_key', models.IntegerField(default=0, verbose_name='Приоритет сортировки')),
            ],
            options={
                'verbose_name': 'Доп. информация',
                'verbose_name_plural': 'Доп. информация',
                'ordering': ('sort_key', 'content'),
            },
        ),
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.CharField(default='tarb3@yandex.ru', max_length=150, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]
