# Generated by Django 2.2.7 on 2019-11-30 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191130_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlow',
            name='zh_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zhilishnik_users', to='main.Zhilishniki', verbose_name='Жилищник'),
        ),
    ]