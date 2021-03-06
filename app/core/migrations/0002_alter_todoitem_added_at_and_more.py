# Generated by Django 4.0.2 on 2022-02-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='added_at',
            field=models.DateTimeField(verbose_name='Added At'),
        ),
        migrations.AddIndex(
            model_name='todoitem',
            index=models.Index(fields=['completed', 'added_at'], name='core_todoit_complet_99f77b_idx'),
        ),
        migrations.AddIndex(
            model_name='todoitem',
            index=models.Index(fields=['added_at'], name='core_todoit_added_a_a0cedd_idx'),
        ),
    ]
