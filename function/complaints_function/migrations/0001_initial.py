# Generated by Django 4.2 on 2025-02-14 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("resident_function", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complaints_model",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "pending"),
                            ("In Progress", "In Progress"),
                            ("Resolved", "resolved"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                (
                    "resident",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resident_function.residents_model",
                    ),
                ),
            ],
            options={
                "db_table": "complaints_table",
            },
        ),
    ]
