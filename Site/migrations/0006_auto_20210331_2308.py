# Generated by Django 3.1.7 on 2021-03-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_keypoint_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keypoint',
            name='preview',
            field=models.CharField(default='dont_set', max_length=89),
        ),
        migrations.AlterField(
            model_name='keypoint',
            name='slug',
            field=models.CharField(default='dont_set', max_length=50),
        ),
    ]