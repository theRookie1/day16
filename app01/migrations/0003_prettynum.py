# Generated by Django 4.0.5 on 2022-07-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_create_time_alter_userinfo_depart'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级'), (5, '5级')], default=1, verbose_name='')),
                ('status', models.SmallIntegerField(choices=[(1, '已占用'), (2, '未使用')], default=2, verbose_name='')),
            ],
        ),
    ]
