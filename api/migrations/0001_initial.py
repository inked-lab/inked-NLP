# Generated by Django 2.2.10 on 2020-02-24 19:21

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawNews',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('article_id', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('article_url', models.URLField()),
                ('origin_url', models.URLField()),
                ('body_html', models.TextField()),
                ('provider', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'raw',
            },
        ),
    ]