# Generated by Django 3.1.7 on 2021-03-31 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0006_auto_20210331_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolLevel',
            fields=[
                ('level', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('startingGrade', models.IntegerField(default=1)),
                ('endingGrade', models.IntegerField(default=3)),
                ('mainSubText', models.TextField()),
                ('subTextHeader', models.CharField(max_length=40)),
                ('subtext', models.TextField()),
            ],
        ),
    ]
