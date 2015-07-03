# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Example: 'flatpages/default.html'", max_length=100, verbose_name='name')),
                ('subject', models.TextField(verbose_name='subject', blank=True)),
                ('subject_es', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('subject_en', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('subject_de', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('subject_it', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('subject_fr', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('subject_pt', models.TextField(null=True, verbose_name='subject', blank=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('content_es', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_en', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_de', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_it', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_fr', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_pt', models.TextField(null=True, verbose_name='content', blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('last_changed', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last changed')),
                ('sites', models.ManyToManyField(to='sites.Site', null=True, verbose_name='sites', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'django_template',
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
            bases=(models.Model,),
        ),
    ]
