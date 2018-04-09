# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickettemplate',
            old_name='name',
            new_name='name_ticket',
        ),
        migrations.AlterField(
            model_name='customization',
            name='ticket_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.TicketTemplate'),
        ),
    ]