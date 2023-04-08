# Generated by Django 4.1.7 on 2023-04-08 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_message_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='base.message'),
        ),
    ]
