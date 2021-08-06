# Generated by Django 3.2.5 on 2021-08-06 07:12

import demo.cipher_field.cipher_field
from django.db import migrations

from demo.cipher_migrate import encrypt_all_field, decrypt_all_field


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20210806_0710'),
    ]

    operations = [
        migrations.RunPython(encrypt_all_field, decrypt_all_field),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=demo.cipher_field.cipher_field.CipherCharField(blank=True, max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA='),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=demo.cipher_field.cipher_field.CipherCharField(blank=True, max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA='),
        ),
    ]