# Generated by Django 4.1.7 on 2023-03-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=20, verbose_name='Название поля 1')),
                ('date', models.DateField(verbose_name='дата 1')),
                ('datetime', models.DateTimeField(verbose_name='дата и время')),
                ('checkbox', models.BooleanField(verbose_name='чек бокс')),
                ('interger', models.IntegerField(verbose_name='число')),
                ('choces', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], verbose_name='выборка')),
            ],
        ),
    ]
