# Generated by Django 3.1.7 on 2021-03-31 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20210331_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='media/keypoints')),
                ('image2', models.ImageField(upload_to='media/keypoints')),
                ('image3', models.ImageField(upload_to='media/keypoints')),
                ('header', models.CharField(max_length=50)),
                ('subtext', models.TextField()),
            ],
        ),
    ]
