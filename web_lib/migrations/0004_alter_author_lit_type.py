# Generated by Django 4.1.5 on 2023-01-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_lib", "0003_product_alter_author_lit_type_store_extuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="lit_type",
            field=models.CharField(
                choices=[("b", "domestic"), ("a", "foreign"), ("c", "other")],
                default="a",
                max_length=1,
                verbose_name="Тип литературы",
            ),
        ),
    ]