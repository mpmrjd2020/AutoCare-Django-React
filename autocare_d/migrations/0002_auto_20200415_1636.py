# Generated by Django 3.0.5 on 2020-04-15 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autocare_d', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service_log',
            options={'ordering': ['service_dt', 'service_type']},
        ),
        migrations.AlterField(
            model_name='service_log',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='autocare_d.Vehicle'),
        ),
        migrations.AlterUniqueTogether(
            name='service_log',
            unique_together={('vehicle', 'service_dt', 'service_type')},
        ),
    ]
