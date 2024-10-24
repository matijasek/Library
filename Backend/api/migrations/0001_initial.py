# Generated by Django 5.1.2 on 2024-10-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'authors_db',
            },
        ),
        migrations.CreateModel(
            name='BooksDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.BigIntegerField()),
                ('isbn', models.CharField(max_length=10)),
                ('isbn13', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('publication_date', models.DateField()),
            ],
            options={
                'db_table': 'books_db',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'libraries_db',
            },
        ),
    ]
