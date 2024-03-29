# Generated by Django 4.2.7 on 2024-01-16 07:48

from django.db import migrations, models
import newsletter_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')),
                ('status', models.CharField(max_length=10, verbose_name='Статус')),
                ('mail_serv_response', models.TextField(verbose_name='Ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, verbose_name='Тема сообщения')),
                ('text', models.TextField(blank=True, verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(default=newsletter_app.models.get_date_now, verbose_name='Дата старта рассылки')),
                ('date_stop', models.DateField(default=newsletter_app.models.get_date_plus_week, verbose_name='Дата завершение рассылки')),
                ('period_send', models.CharField(choices=[('DAILY', 'Раз в день'), ('WEEKLY', 'Раз в неделю'), ('MONTHLY', 'Раз в месяц')], default='WEEKLY', max_length=20, verbose_name='Периодичность')),
                ('status_send', models.CharField(choices=[('CREATED', 'Создана'), ('STARTED', 'Запущена'), ('COMPLETED', 'Завершена')], default='CREATED', max_length=20, verbose_name='Статус рассылки')),
                ('client', models.ManyToManyField(to='newsletter_app.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'permissions': [('set_status_send', 'Can change status_send')],
            },
        ),
    ]
