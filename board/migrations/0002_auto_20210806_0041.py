# Generated by Django 3.2.4 on 2021-08-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]