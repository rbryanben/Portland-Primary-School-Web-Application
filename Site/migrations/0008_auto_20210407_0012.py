# Generated by Django 3.1.7 on 2021-04-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0007_facilitiespagecontent_schoolfacility'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfacility',
            name='focusText',
            field=models.TextField(default='this should be the text that appears when displays in the first 4'),
        ),
        migrations.AddField(
            model_name='schoolfacility',
            name='focusTitle',
            field=models.TextField(default='this should be the header that appears when displays in the first 4'),
        ),
    ]
