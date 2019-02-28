# Generated by Django 2.1.3 on 2019-02-24 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('body', models.TextField()),
                ('published', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[
                 ('d', 'Draft'), ('p', 'Published')], default='d', max_length=20)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]