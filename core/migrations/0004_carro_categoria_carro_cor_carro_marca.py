# Generated by Django 4.1 on 2022-08-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='carro', to='core.categoria'),
        ),
        migrations.AddField(
            model_name='carro',
            name='cor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='carro', to='core.cor'),
        ),
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='carro', to='core.marca'),
        ),
    ]