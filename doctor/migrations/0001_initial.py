# Generated by Django 4.1.3 on 2024-02-15 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('pharmacist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.TextField(max_length=10)),
                ('patient_no', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_id', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.patient')),
                ('prescribe_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.users')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_served', models.DateTimeField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
                ('served_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.users')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_unit', models.IntegerField()),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacist.drug')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
    ]