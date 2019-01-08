# Generated by Django 2.1.1 on 2019-01-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190105_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply_name',
            field=models.CharField(default=None, max_length=50, verbose_name='回复的哪个人'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='root_to',
            field=models.IntegerField(default=0, verbose_name='回复的是哪个主评论'),
        ),
    ]