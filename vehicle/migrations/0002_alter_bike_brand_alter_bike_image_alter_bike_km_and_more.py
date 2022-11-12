# Generated by Django 4.1.2 on 2022-10-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='Brand',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bike',
            name='Image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='KM',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bike',
            name='Title',
            field=models.CharField(blank=True, max_length=20000),
        ),
    ]