# Generated by Django 3.2.5 on 2021-07-23 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_reservation_invoices'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomReserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
            options={
                'unique_together': {('reservation', 'room')},
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='rooms',
            field=models.ManyToManyField(through='api.RoomReserved', to='api.Room'),
        ),
    ]