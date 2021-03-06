# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memorytotal', models.IntegerField(verbose_name='内存总量')),
                ('memoryrate', models.DecimalField(decimal_places=2, max_digits=4, max_length=10, verbose_name='内存使用率')),
                ('disktotal', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='硬盘总量')),
                ('diskrate', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='硬盘使用率')),
            ],
            options={
                'db_table': 'alldata',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '事业部门',
                'verbose_name_plural': '事业部门',
                'db_table': 'businessunit',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('to_b', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ipdata.BusinessUnit')),
            ],
            options={
                'verbose_name': '环境类型',
                'verbose_name_plural': '环境类型',
                'db_table': 'environment',
            },
        ),
        migrations.CreateModel(
            name='IpConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='ip名称')),
                ('type', models.SmallIntegerField(choices=[(0, 'service'), (1, 'big_data')], default=0, verbose_name='服务器类型')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipdata.Environment', verbose_name='环境')),
            ],
            options={
                'verbose_name': 'IP配置',
                'verbose_name_plural': 'IP配置',
                'db_table': 'ipconfig',
            },
        ),
        migrations.CreateModel(
            name='IpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ip名称')),
                ('memorytotal', models.IntegerField(verbose_name='内存总量')),
                ('memoryuse', models.IntegerField(verbose_name='内存使用量')),
                ('memoryrate', models.DecimalField(decimal_places=2, max_digits=4, max_length=10, verbose_name='内存使用率')),
                ('cpucore', models.IntegerField(default=4, verbose_name='cpu核数量')),
                ('averageload', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='平均load值')),
                ('disktotal', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='磁盘总量')),
                ('diskrate', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='硬盘使用率')),
                ('diskuse', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='磁盘使用量')),
                ('servertype', models.SmallIntegerField(choices=[(0, '虚拟机'), (1, '物理机')], default=0, verbose_name='类型')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipdata.Environment', verbose_name='环境')),
            ],
            options={
                'db_table': 'ipinfo',
            },
        ),
        migrations.CreateModel(
            name='RecordingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(verbose_name='历史⽇期')),
            ],
            options={
                'db_table': 'recordingtime',
            },
        ),
        migrations.AddField(
            model_name='ipinfo',
            name='times',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipdata.RecordingTime', verbose_name='时间'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipdata.Environment', verbose_name='环境'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipdata.RecordingTime', verbose_name='时间'),
        ),
    ]
