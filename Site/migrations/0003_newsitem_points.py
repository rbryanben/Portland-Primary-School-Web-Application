# Generated by Django 3.1.7 on 2021-04-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_newsitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='points',
            field=models.TextField(default='not_set'),
        ),
    ]