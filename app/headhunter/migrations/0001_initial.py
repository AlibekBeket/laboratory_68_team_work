# Generated by Django 4.2 on 2023-04-20 00:01

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
            name='VacancyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория вакансии',
                'verbose_name_plural': 'Категории вакансий',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('salary', models.PositiveIntegerField(verbose_name='Зарплата')),
                ('description', models.TextField(verbose_name='Детальное описание')),
                ('experience_time', models.PositiveIntegerField(verbose_name='Опыт работы (лет)')),
                ('is_active', models.BooleanField(default=False, verbose_name='Опубликовать вакансию')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Время удаления')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('vacancy_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='headhunter.vacancycategory', verbose_name='Категория вакансии')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
