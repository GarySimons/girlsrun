# Generated by Django 3.0.8 on 2020-08-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herstory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=200)),
                ('story', models.CharField(max_length=50)),
            ],
        ),
    ]