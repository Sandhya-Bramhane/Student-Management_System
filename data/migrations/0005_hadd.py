# Generated by Django 4.2 on 2024-02-07 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('dt', models.CharField(max_length=20)),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=20)),
                ('mo', models.CharField(max_length=20)),
                ('co', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=20)),
                ('du', models.CharField(max_length=20)),
            ],
        ),
    ]