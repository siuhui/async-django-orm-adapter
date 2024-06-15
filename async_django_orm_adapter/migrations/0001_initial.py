
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CasbinRule",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ptype", models.CharField(max_length=255)),
                ("v0", models.CharField(max_length=255)),
                ("v1", models.CharField(max_length=255)),
                ("v2", models.CharField(max_length=255)),
                ("v3", models.CharField(max_length=255)),
                ("v4", models.CharField(max_length=255)),
                ("v5", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "casbin_rule",
            },
        ),
    ]
