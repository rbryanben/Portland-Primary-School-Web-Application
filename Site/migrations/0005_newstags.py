# Generated by Django 3.1.7 on 2021-04-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_newsitem_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsTags',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
    ]