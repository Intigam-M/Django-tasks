# Generated by Django 4.1 on 2022-08-13 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('expirate', models.DateField()),
                ('recipe_needed', models.BooleanField(default=False)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacyapp.factory')),
            ],
        ),
    ]
