# Generated by Django 4.0.5 on 2022-07-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pylib', '0003_alter_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
