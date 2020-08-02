from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=50, blank=False, verbose_name='Полное имя')
    birth_year = models.CharField(max_length=4, verbose_name='Год рождения')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Debtor(models.Model):
    full_name = models.CharField(max_length=50, blank=False, verbose_name='Имя должника')
    book = models.ManyToManyField('Book', related_name='book', blank=True, verbose_name='Должник')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'


class PublishingHouse(models.Model):
    pub_name = models.CharField(max_length=20, blank=False, verbose_name='Название издательства')

    def __str__(self):
        return self.pub_name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Book(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Название книги')
    year = models.CharField(max_length=4, verbose_name='Год издания')
    pub_house = models.ManyToManyField(PublishingHouse, related_name='book', blank=True, verbose_name='Издательство')
    author = models.ManyToManyField(Author, related_name='book', blank=True, verbose_name='Автор')
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость в рублях')
    count = models.SmallIntegerField(default=1, blank=False, verbose_name='Количество')
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name='Обложка')

    def get_image(self):
        if not self.cover:
            self.cover = 'covers/no_img.jpg'
            return self.cover
        else:
            return self.cover

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
