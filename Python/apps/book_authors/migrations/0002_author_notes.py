# Generated by Django 2.0 on 2017-12-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(default='notes', max_length=255),
            preserve_default=False,
        ),
    ]
