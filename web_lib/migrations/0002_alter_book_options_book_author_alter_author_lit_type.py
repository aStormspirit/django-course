# Generated by Django 4.1.5 on 2023-01-08 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web_lib", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "get_latest_by": "published",
                "verbose_name": "Книги",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="web_lib.author",
            ),
            preserve_default=False,
        ),
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
