# Generated by Django 3.2.7 on 2022-08-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_cards_card_meaning_ukr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_meaning_ukr',
            field=models.TextField(),
        ),
    ]
