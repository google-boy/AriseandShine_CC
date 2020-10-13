# Generated by Django 3.1.2 on 2020-10-11 08:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('v', 'voluntary'), ('i', 'internship'), ('p', 'Permanent'), ('c', 'Contract'), ('u', 'uncategorized')], default='u', max_length=1)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('application_deadline', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='job start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='job end date')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=50)),
                ('donor_category', models.CharField(blank=True, choices=[('ind', 'Individual'), ('org', 'Organization'), ('gov', 'Government'), ('unc', 'Uncategorized')], default='unc', max_length=3)),
                ('pledge', models.CharField(blank=True, max_length=100, null=True)),
                ('other_information', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/logos')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(help_text='Filesize should not be more than 5mb, Compress first if otherwise', upload_to='images/%Y/%m/%d/')),
                ('caption', models.CharField(help_text='Provide a caption text of not more than 256 characters', max_length=256, verbose_name='picture caption')),
                ('carousel', models.BooleanField(default=False, help_text='Select this check to show this picture on the homepage slideshow', verbose_name='display on the carousel')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('other_names', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number', models.CharField(max_length=15, unique=True)),
                ('date_of_birth', models.DateField(blank=True, default='1970-07-01')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter phone number in the international format<br>e.g +2547xxxxxxxx', max_length=128, region=None)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('occupation', models.CharField(blank=True, max_length=15, null=True)),
                ('designation', models.CharField(blank=True, default='member', max_length=50)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50, verbose_name='name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('time_of_receipt', models.DateTimeField(auto_now_add=True, verbose_name='received on')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=50)),
                ('partner_category', models.CharField(blank=True, choices=[('Gov', 'Government Entity'), ('NGO', 'Non-Governmental Organization'), ('CBO', 'Community Based Organization'), ('SHP', 'Self-Help Group'), ('UNC', 'Uncategorized')], default='UNC', max_length=3)),
                ('more_info', models.TextField(blank=True, null=True, verbose_name='More information')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/logos')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='Arise and shine Care Centre', max_length=50)),
                ('about', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('slogan', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Arise and Shine Profile',
                'verbose_name_plural': 'Arise and Shine Profile',
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_value', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.profile')),
            ],
            options={
                'verbose_name': 'Core value',
                'verbose_name_plural': 'Core values',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('thematic_area', models.CharField(choices=[('livelihood', 'Livelihood'), ('health', 'Health'), ('education', 'Education'), ('environment', 'Environment'), ('social-Protection', 'Social Protection')], max_length=17)),
                ('project_description', models.TextField()),
                ('start_date', models.DateField(verbose_name='Started')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Ended')),
                ('donations', models.ManyToManyField(blank=True, help_text='Select donors for this project if any', to='mainsite.Donation')),
                ('media', models.ManyToManyField(blank=True, to='mainsite.Media')),
                ('partners', models.ManyToManyField(blank=True, help_text='Select partners for this project if any', to='mainsite.Partner')),
            ],
            options={
                'ordering': ['-start_date', 'end_date'],
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
                ('profile', models.ForeignKey(help_text="State the cbo's profile for this objective", null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.profile')),
            ],
        ),
        migrations.CreateModel(
            name='NewsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('external_link', models.URLField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(help_text='If you enter a future date, the event will be posted on that date you have entered', verbose_name='publication date')),
                ('media', models.ManyToManyField(blank=True, help_text='Choose a picture for this news or event', to='mainsite.Media')),
            ],
            options={
                'verbose_name': 'News and Event',
                'verbose_name_plural': 'News and Events',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Job_Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.career')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.CharField(max_length=200)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.career')),
            ],
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact_text', models.TextField(verbose_name='impact')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter phone number in the international format<br>e.g +2547xxxxxxxx', max_length=128, region=None)),
                ('whatsapp', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter the whatsapp number in the international format<br>e.g +2547xxxxxxxx', max_length=128, region=None)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.ForeignKey(help_text="State the cbo's profile for these contacts", null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_address', models.CharField(max_length=100)),
                ('postal_address', models.PositiveSmallIntegerField()),
                ('postal_code', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=50, verbose_name='City/Town')),
                ('site_map', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.ForeignKey(help_text='You need to state explicitly the current profile of the cbo for this address', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.profile')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
