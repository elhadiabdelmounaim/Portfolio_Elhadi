from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0004_cvitem_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="subject",
            field=models.CharField(max_length=160),
        ),
    ]
