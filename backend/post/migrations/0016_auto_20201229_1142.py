# Generated by Django 3.1.4 on 2020-12-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_customuser_last_date_sent_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='send_date',
            new_name='create_date',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_date_sent_mail',
            field=models.DateTimeField(auto_now_add=True, db_column='sent_date'),
        ),
    ]
