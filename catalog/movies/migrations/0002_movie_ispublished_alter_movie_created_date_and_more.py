# Generated by Django 4.1 on 2022-09-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isPublished',
            field=models.BooleanField(default=True, verbose_name='Yayında mı?'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='Film Açıklaması'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Film Resmi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Film Adı'),
        ),
    ]
