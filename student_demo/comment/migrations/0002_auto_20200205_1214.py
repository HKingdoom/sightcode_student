# Generated by Django 2.0.6 on 2020-02-05 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '作业提交', 'verbose_name_plural': '作业提交'},
        ),
    ]