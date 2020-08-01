# Generated by Django 3.0.8 on 2020-08-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200731_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('fine', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='fine',
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='default_name', max_length=40),
            preserve_default=False,
        ),
    ]