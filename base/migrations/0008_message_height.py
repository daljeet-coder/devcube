# Generated by Django 4.1.7 on 2023-04-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_message_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='height',
            field=models.IntegerField(default=0),
        ),
    ]