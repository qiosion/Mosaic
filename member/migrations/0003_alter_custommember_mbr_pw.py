# Generated by Django 4.2.1 on 2023-05-31 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0002_alter_custommember_groups_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="custommember",
            name="mbr_pw",
            field=models.CharField(default="", max_length=100),
        ),
    ]
