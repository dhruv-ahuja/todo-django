# Generated by Django 4.0.2 on 2022-02-14 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_todoitem_options_todoitem_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['completed'],
            },
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['completed', 'added_at'], name='core_task_complet_2bfa8a_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['added_at'], name='core_task_added_a_6d7092_idx'),
        ),
    ]