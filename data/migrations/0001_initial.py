# Generated by Django 4.2.3 on 2023-11-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('pass1', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
    ]
