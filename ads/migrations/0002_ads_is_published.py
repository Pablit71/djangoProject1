# Generated by Django 4.1 on 2022-08-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ads",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name=True),
            preserve_default=False,
        ),
    ]