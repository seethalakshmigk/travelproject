# Generated by Django 4.2.5 on 2023-09-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pimage', models.ImageField(upload_to='pics')),
                ('pdesc', models.TextField(max_length=100)),
            ],
        ),
    ]
