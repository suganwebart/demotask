# Generated by Django 5.0.6 on 2024-06-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0004_alter_book_description_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]