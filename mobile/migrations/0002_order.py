# Generated by Django 3.1.7 on 2021-05-09 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=150)),
                ('user', models.CharField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.product')),
            ],
        ),
    ]
