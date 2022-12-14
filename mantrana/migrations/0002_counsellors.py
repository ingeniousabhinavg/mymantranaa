# Generated by Django 4.1 on 2022-09-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantrana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counsellors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(max_length=50, upload_to='counsellors')),
                ('joined_on', models.DateField()),
                ('experties', models.CharField(max_length=100)),
            ],
        ),
    ]
