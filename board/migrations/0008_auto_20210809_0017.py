# Generated by Django 3.2.4 on 2021-08-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20210809_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]