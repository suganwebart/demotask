# Generated by Django 5.0.6 on 2024-06-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0003_alter_genre_options_alter_role_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]
