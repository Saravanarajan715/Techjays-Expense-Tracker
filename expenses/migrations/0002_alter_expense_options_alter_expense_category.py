# Generated by Django 5.1.1 on 2024-10-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Healthcare', 'Healthcare'), ('Shopping', 'Shopping'), ('Other', 'Other')], max_length=50),
        ),
    ]
