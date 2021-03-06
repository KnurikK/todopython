# Generated by Django 3.1.4 on 2021-04-22 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210420_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=350)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pub_year', models.DateField(auto_now_add=True)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='BookStore',
        ),
    ]
