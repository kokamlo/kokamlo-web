# Generated by Django 3.2.5 on 2021-07-12 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jafar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='profo/image/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
