# Generated by Django 4.0.2 on 2022-02-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_todoitem_added_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='added_at',
            field=models.DateTimeField(),
        ),
    ]
