# Generated by Django 5.1.4 on 2025-01-04 13:32

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
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=5000)),
                ('is_answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=10000)),
                ('question_type', models.CharField(max_length=20)),
                ('required', models.BooleanField(default=False)),
                ('answer_key', models.CharField(blank=True, max_length=5000)),
                ('score', models.IntegerField(blank=True, default=0)),
                ('feedback', models.CharField(max_length=5000, null=True)),
                ('choices', models.ManyToManyField(related_name='question_choices', to='form.choices')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('background_color', models.CharField(default='#d9efed', max_length=20)),
                ('text_color', models.CharField(default='#272124', max_length=20)),
                ('collect_email', models.BooleanField(default=False)),
                ('authenticated_responder', models.BooleanField(default=False)),
                ('edit_after_submit', models.BooleanField(default=False)),
                ('confirmation_message', models.CharField(default='Your response has been recorded.', max_length=10000)),
                ('is_quiz', models.BooleanField(default=False)),
                ('allow_view_score', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('questions', models.ManyToManyField(related_name='forms', to='form.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000)),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='form.questions')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions_set', to='auth.permission')),
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
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_code', models.CharField(max_length=20)),
                ('responder_ip', models.CharField(max_length=30)),
                ('responder_email', models.EmailField(blank=True, max_length=254)),
                ('response', models.ManyToManyField(related_name='answer_responses', to='form.answer')),
                ('response_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_responses', to='form.form')),
                ('responder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_responses', to='form.user')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_forms', to='form.user'),
        ),
    ]