# Generated by Django 3.0.7 on 2020-06-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_auto_20200618_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
