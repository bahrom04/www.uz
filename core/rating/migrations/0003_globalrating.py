# Generated by Django 4.2.8 on 2023-12-04 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_alter_category_title_alter_subcategory_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.website')),
            ],
            options={
                'verbose_name': 'GlobalRating',
                'verbose_name_plural': 'GlobalRatings',
            },
        ),
    ]
