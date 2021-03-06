# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-14 20:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[(b'1', b'General'), (b'2', b'Management'), (b'3', b'Compensation'), (b'4', b'Suggestions'), (b'5', b'Complaint')], default=b'1', max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=150, validators=[django.core.validators.EmailValidator(), django.core.validators.MinLengthValidator(7), django.core.validators.MaxLengthValidator(10, message=b'too long')]),
        ),
    ]
