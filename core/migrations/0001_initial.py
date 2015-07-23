# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.FloatField()),
                ('promotion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_shipping', models.CharField(max_length=100)),
                ('street1_shipping', models.CharField(max_length=200)),
                ('street2_shipping', models.CharField(max_length=200)),
                ('city_shipping', models.CharField(max_length=50)),
                ('state_shipping', models.CharField(max_length=50)),
                ('zipcode_shipping', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('shipping_cost', models.FloatField()),
                ('total_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('color', models.ForeignKey(to='core.Color')),
                ('price', models.ForeignKey(to='core.Price')),
            ],
        ),
        migrations.CreateModel(
            name='SpongeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='sponge',
            name='type',
            field=models.ForeignKey(to='core.SpongeType'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='sponges',
            field=models.ManyToManyField(related_name='receipt_sponges_set', to='core.Sponge'),
        ),
        migrations.AddField(
            model_name='order',
            name='receipt',
            field=models.ForeignKey(to='core.Receipt'),
        ),
        migrations.AlterUniqueTogether(
            name='sponge',
            unique_together=set([('color', 'type')]),
        ),
    ]
