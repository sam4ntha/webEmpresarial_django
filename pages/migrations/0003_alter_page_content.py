# Generated by Django 4.2.1 on 2023-06-05 06:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_options_page_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=200, verbose_name='Contenido'),
        ),
    ]