# Generated by Django 4.2.3 on 2023-10-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quillcart', '0004_remove_book_id_alter_book_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='custom_id',
            field=models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False),
        ),
    ]
