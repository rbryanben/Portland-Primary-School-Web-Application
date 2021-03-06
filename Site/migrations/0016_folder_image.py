# Generated by Django 3.1.7 on 2021-04-11 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0015_topstudent_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('imageBase', models.ImageField(upload_to='media/filing/folders')),
                ('note', models.TextField(default='A folder cannot contain both a folder and images, just 1 of the two')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.folder')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageFile', models.ImageField(upload_to='media/filing/images')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.folder')),
            ],
        ),
    ]
