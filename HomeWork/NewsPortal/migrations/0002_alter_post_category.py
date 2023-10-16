# Generated by Django 4.2.6 on 2023-10-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='article', through='NewsPortal.PostCategory', to='NewsPortal.category'),
        ),
    ]
