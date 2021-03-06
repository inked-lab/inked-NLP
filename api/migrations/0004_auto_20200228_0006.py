# Generated by Django 2.2.10 on 2020-02-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200227_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawnews',
            name='article_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rawnews',
            name='article_url',
            field=models.URLField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='rawnews',
            name='origin_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='rawnews',
            name='provider',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rawnews',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
