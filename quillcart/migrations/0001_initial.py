# Generated by Django 4.2.3 on 2023-10-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('custom_id', models.DecimalField(decimal_places=0, max_digits=13, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('authors', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('category', models.CharField(max_length=255)),
                ('distribution_expense', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
