# Generated by Django 4.1.3 on 2022-11-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_list', '0008_alter_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
