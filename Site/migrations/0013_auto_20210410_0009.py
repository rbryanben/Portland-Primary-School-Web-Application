# Generated by Django 3.1.7 on 2021-04-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0012_auto_20210407_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicsPageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backImage', models.ImageField(upload_to='media/academics')),
                ('mainHeader', models.TextField(default='Best Primary Education')),
                ('mainSubtext', models.TextField(default='Emply dummy text of the printing and typesetting industry has been dummy text ever sicnce type setting idustry')),
                ('bodyText', models.TextField(default='But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?')),
            ],
        ),
        migrations.CreateModel(
            name='TopStudent',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='media/academics/top_students')),
                ('remarks', models.TextField(default='Magret Khumalo was at the top of her class last year 2019, coming out with 5 units in Mathematics, Agriculture, English, General Paper and Ndebele')),
            ],
        ),
        migrations.RemoveField(
            model_name='schoolfacility',
            name='qoute',
        ),
    ]
