# Generated by Django 2.2.9 on 2020-02-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20200213_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos'),
        ),
    ]
