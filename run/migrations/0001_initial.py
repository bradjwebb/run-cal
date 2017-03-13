# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 04:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('title', models.TextField(editable=False)),
                ('run_type', models.CharField(max_length=2)),
                ('pace_fast', models.DurationField()),
                ('pace_slow', models.DurationField()),
                ('pace_mid', models.DurationField()),
                ('elapsed_time', models.DurationField()),
                ('special', models.TextField()),
                ('run_date', models.DateTimeField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]