# Generated by Django 3.1.4 on 2021-06-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_data_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('articleId', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
