# Generated by Django 2.1.7 on 2019-02-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prefMovie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, height_field='picture_height', max_length=255, null=True, upload_to='images/movies/', width_field='picture_width'),
        ),
    ]