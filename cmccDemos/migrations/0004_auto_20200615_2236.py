# Generated by Django 3.0.7 on 2020-06-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmccDemos', '0003_auto_20200312_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmccdemo',
            name='new_field',
            field=models.CharField(default='SOME STRING', max_length=5000),
        ),
    ]