# Generated by Django 3.1.14 on 2022-03-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('shop', '0009_auto_20220305_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ManyToManyField(to='author.AuthorProfile'),
        ),
    ]
