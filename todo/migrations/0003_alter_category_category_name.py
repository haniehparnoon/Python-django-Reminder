# Generated by Django 3.2.9 on 2021-12-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
    ]
