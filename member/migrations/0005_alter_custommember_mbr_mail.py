# Generated by Django 4.2.1 on 2023-06-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0004_alter_custommember_mbr_pw"),
    ]

    operations = [
        migrations.AlterField(
            model_name="custommember",
            name="mbr_mail",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]