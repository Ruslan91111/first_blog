from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    title_tag = models.CharField(max_length=255, verbose_name='Тэг-лайн')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(verbose_name='текст')
    post_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    category = models.CharField(max_length=255, verbose_name='Категория', default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts', verbose_name='Нравится')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        # return reverse('article-detail', args=(str(self.id)))











