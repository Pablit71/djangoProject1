# Generated by Django 4.1 on 2022-08-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_remove_ads_is_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="ads",
            name="is_published",
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
