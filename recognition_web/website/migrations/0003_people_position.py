# Generated by Django 2.1.3 on 2018-11-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20181127_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='position',
            field=models.CharField(default='Glober', max_length=100),
        ),
    ]
