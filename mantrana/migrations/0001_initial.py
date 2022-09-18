# Generated by Django 4.1 on 2022-09-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('banner', models.ImageField(upload_to='services')),
                ('about', models.TextField()),
                ('created_on', models.DateField()),
            ],
        ),
    ]
