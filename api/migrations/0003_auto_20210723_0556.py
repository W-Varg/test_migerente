# Generated by Django 3.2.5 on 2021-07-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210723_0549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={},
        ),
        migrations.CreateModel(
            name='InvoiceGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('date_paid', models.DateField()),
                ('date_canceled', models.DateField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.guest')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
            ],
            options={
                'unique_together': {('guest', 'reservation')},
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='invoices',
            field=models.ManyToManyField(related_name='invoices_guest', through='api.InvoiceGuest', to='api.Guest'),
        ),
    ]