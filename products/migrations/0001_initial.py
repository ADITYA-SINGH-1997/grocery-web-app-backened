# Generated by Django 3.0.5 on 2020-11-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(default='Empty description.', max_length=500)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products/images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('quantity', models.IntegerField(default=10)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
