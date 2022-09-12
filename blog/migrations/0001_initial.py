# Generated by Django 4.1.1 on 2022-09-06 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('category', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack')], max_length=9)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=9)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
