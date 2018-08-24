# Generated by Django 2.1 on 2018-08-24 17:01

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum 75 characters', max_length=75, verbose_name='Title')),
                ('picture', models.FileField(blank=True, null=True, upload_to='Categories/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum 75 characters', max_length=75, verbose_name='Title')),
                ('content', models.TextField(help_text='Maximum 1000 characters', max_length=1000, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Maximum 75 characters', max_length=75, verbose_name='Food name')),
                ('picture', models.FileField(blank=True, null=True, upload_to='Foods/')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('userWeight', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='User Weight')),
                ('customWeight', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Custom Weight')),
                ('details', models.TextField(blank=True, help_text='Maximum 1000 characters', max_length=1000, null=True, verbose_name='Details')),
                ('categories', models.ManyToManyField(blank=True, related_name='FoodCategory', to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.NullBooleanField(default=False, verbose_name='Status')),
                ('submitDateTime', models.DateTimeField(auto_now_add=True, verbose_name='Submit date time')),
                ('orderDateTime', models.DateField(blank=True, default='2018-08-24', verbose_name='Order date time')),
                ('details', models.TextField(blank=True, help_text='Maximum 1000 characters', max_length=1000, null=True, verbose_name='Details')),
                ('food', models.ManyToManyField(related_name='Food', to='api.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserOrder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Maximum 75 characters', max_length=75, verbose_name='Restaurant name')),
                ('picture', models.FileField(blank=True, null=True, upload_to='Restaurants/')),
                ('menuPicture', models.FileField(blank=True, null=True, upload_to='Restaurants/')),
                ('userWeight', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='User Weight')),
                ('customWeight', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Custom Weight')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RestaurantFood', to='api.Restaurant'),
        ),
        migrations.AddField(
            model_name='comment',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FoodComments', to='api.Food'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserComments', to=settings.AUTH_USER_MODEL),
        ),
    ]
