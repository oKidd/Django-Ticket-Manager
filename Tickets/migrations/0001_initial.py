# Generated by Django 4.1.1 on 2022-12-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
        ),
    ]
