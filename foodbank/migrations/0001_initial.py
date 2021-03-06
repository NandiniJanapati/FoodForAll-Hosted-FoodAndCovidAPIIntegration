# Generated by Django 4.0.3 on 2022-04-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('DonationID', models.AutoField(primary_key=True, serialize=False)),
                ('DonationName', models.CharField(max_length=500)),
                ('DonationAllergies', models.CharField(max_length=500)),
                ('DonationFoodBank', models.CharField(max_length=500)),
                ('DonationQuantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationToFoodBank',
            fields=[
                ('BridgeID', models.AutoField(primary_key=True, serialize=False)),
                ('FoodBankIDVal', models.CharField(max_length=500)),
                ('DonationIDVal', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FoodBanks',
            fields=[
                ('FoodBankID', models.AutoField(primary_key=True, serialize=False)),
                ('FoodBankZipCode', models.CharField(max_length=500)),
                ('FoodBankCity', models.CharField(max_length=500)),
                ('FoodBankName', models.CharField(max_length=500)),
                ('FoodBankAddress', models.CharField(max_length=500)),
            ],
        ),
    ]
