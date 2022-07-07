from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField('Назва', max_length=100)
    anons = models.CharField('Анонс', max_length=100)
    full_text = models.TextField('Новина')
    image_post = models.ImageField(upload_to='image/pdfs/', null=True, blank=True)
    date = models.DateTimeField('Дата Публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Новини'


class LikeNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)