# Generated by Django 5.1.5 on 2025-02-21 07:58

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegisterShipForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('vessel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('flag', models.CharField(blank=True, max_length=100, null=True)),
                ('year_built', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('LOA', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ship_image')),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='ship_image')),
                ('is_status', models.BooleanField(default=False)),
                ('hidden_details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category_image')),
                ('category_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterShipForCharter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('inspection_country', models.CharField(blank=True, max_length=100, null=True)),
                ('year_built', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('desirable_capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('Class', models.CharField(blank=True, max_length=100, null=True)),
                ('buy_as_scrap', models.CharField(blank=True, max_length=100, null=True)),
                ('from_price', models.CharField(blank=True, max_length=100, null=True)),
                ('to_price', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ship_image')),
                ('is_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterShipForEquipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('is_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CstmUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image')),
                ('address', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('ship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='web.adminregistershipforsale')),
            ],
        ),
        migrations.AddField(
            model_name='adminregistershipforsale',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category'),
        ),
        migrations.CreateModel(
            name='RegisterShipForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('vessel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('flag', models.CharField(blank=True, max_length=100, null=True)),
                ('year_built', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('capacity', models.CharField(blank=True, max_length=100, null=True)),
                ('LOA', models.CharField(blank=True, max_length=100, null=True)),
                ('Class', models.CharField(blank=True, max_length=100, null=True)),
                ('GRT_NRT', models.CharField(blank=True, max_length=100, null=True)),
                ('Teu', models.CharField(blank=True, max_length=100, null=True)),
                ('main_engine', models.CharField(blank=True, max_length=100, null=True)),
                ('DWT', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ship_image')),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='thumbnail_image')),
                ('is_status', models.BooleanField(default=False)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('sub_category_description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
        ),
    ]
