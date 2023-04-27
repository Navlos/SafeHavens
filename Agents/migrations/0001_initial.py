# Generated by Django 4.1.4 on 2023-01-11 01:26

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
            name='Agent',
            fields=[
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('profile_image', models.ImageField(blank=True, default='images/defalt.png', null=True, upload_to='profile_images/')),
                ('state', models.CharField(choices=[('Abia_state', 'Abia'), ('Adamawa_state', 'Adamawa'), ('Akwa_Ibom_state', 'Akwa Ibom'), ('Anambra_state', 'Anambra'), ('Bauchi_state', 'Bauchi'), ('Bayelsa_state', 'Bayelsa'), ('Benue_state', 'Benue'), ('Borno_state', 'Borno'), ('Cross_River_state', 'Cross River'), ('Delta_state', 'Delta'), ('Eboniyi_state', 'Eboniyi'), ('Edo_state', 'Edo'), ('Ekiti_state', 'Ekiti'), ('Enugu_state', 'Enugu'), ('Gombe_state', 'Gombe'), ('Imo_state', 'Imo'), ('Jigawa_state', 'Jigawa'), ('Kaduna_state', 'Kaduna'), ('Kano_state', 'Kano'), ('Katsina_state', 'Katsina'), ('Kebbi_state', 'Kebbi'), ('Kogi_state', 'Kogi'), ('Kwara_state', 'Kwara'), ('Lagos_state', 'Lagos'), ('Nassarawa_state', 'Nassarawa'), ('Niger_state', 'Niger'), ('Ogun_state', 'Ogun'), ('Ondo_state', 'Ondo'), ('Osun_state', 'Osun'), ('Oyo_state', 'Oyo'), ('Plateau_state', 'Plateau'), ('Rivers_state', 'Rivers'), ('Sokoto_state', 'Sokoto'), ('Taraba_state', 'Taraba'), ('Yobe_state', 'Yobe'), ('Zamfara_state', 'Zamfara'), ('Federal_Capital_Territory', 'Federal Capital Territory')], max_length=30)),
                ('description', models.TextField()),
                ('form_filled', models.BooleanField(default=False)),
                ('accomodation_counter', models.PositiveIntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
