from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Час оновлення')
    photo = models.ImageField(upload_to='photos/%Y%m%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Стан публікації')
    category = models.ForeignKey('Category', verbose_name='Категорія', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'категорії'
        ordering = ['title']