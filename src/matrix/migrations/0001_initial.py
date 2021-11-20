# Generated by Django 3.2.9 on 2021-11-20 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25, verbose_name='Text')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='matrix.collection', verbose_name='Collection')),
            ],
        ),
    ]