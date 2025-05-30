# Generated by Django 5.0.7 on 2024-08-04 09:46

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishu', '0003_beverages_prices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverages',
            name='prices',
            field=models.CharField(default='Re', max_length=10),
        ),
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_no', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_untill', models.DateTimeField(default=datetime.datetime(2026, 8, 6, 9, 46, 10, 923054, tzinfo=datetime.timezone.utc))),
                ('drink', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='ishu.beverages')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ishu.beverages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('drink_varieties', models.ManyToManyField(related_name='stores', to='ishu.beverages')),
            ],
        ),
    ]
