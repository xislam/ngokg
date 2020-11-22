from django.db import models

# Create your models here.


class News(models.Model):
    # модель для новостей
    dt = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    title = models.TextField(max_length=3000, verbose_name="Заглавие")
    img = models.FileField(null=True, blank=True, upload_to="img", verbose_name="картинка")
    link = models.URLField()
    desc = models.TextField(max_length=10000, verbose_name="описание")
    site_name = models.CharField(max_length=300, verbose_name="Наименование сайта")
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class RankLibrary(models.Model):
    # модель категории для млдели LibraryFromNGO
    name = models.CharField(max_length=500, verbose_name="name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория библиотеки'
        verbose_name_plural = 'Категория библиотеки'


class LibraryFromNGO(models.Model):
    # модель для библиотека об НКО
    rank = models.ForeignKey(RankLibrary, on_delete=models.CASCADE,
                             related_name='related_to_library', verbose_name='Категории')
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(max_length=5000, verbose_name="Описание")
    files = models.FileField(upload_to='documents', verbose_name="Файл")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    # доп модель категории
    # пиши виюсеты лист и дитайл

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Библиотека НКО'
        verbose_name_plural = 'Библиотека НКО'


class RankLegislation(models.Model):
    # модель категории для млдели Legislation
    name = models.CharField(max_length=500, verbose_name="Название")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория законодательство'
        verbose_name_plural = 'Категории законодательств'


class Legislation(models.Model):
    # модель для законодательств
    rank = models.ForeignKey(RankLegislation, on_delete=models.CASCADE,
                             related_name='related_to_library', verbose_name='Категории')
    name = models.CharField(max_length=300, verbose_name="Название законодательство об НКО")
    description = models.TextField(max_length=8000, verbose_name="Описание")
    files = models.FileField(upload_to='documents')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')
    # доп модель категории
    # пиши виюсеты лист и дитайл

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Законодательство'
        verbose_name_plural = 'Законодательство'


class QA(models.Model):
    # часто задаваемые вапросы
    name = models.CharField(max_length=1000, verbose_name='Вопрос')
    description = models.TextField(max_length=8000, verbose_name="description")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    edited_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Дата редактирования')
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос & Ответ'
        verbose_name_plural = 'Вопросы & Ответы'


class Question(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    mail = models.CharField(max_length=80, verbose_name='Почта')
    text = models.TextField(max_length=2000, verbose_name='Вопрос')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Review(models.Model):
    stars = models.IntegerField(verbose_name='Звезды')
    text = models.TextField(max_length=2000, verbose_name='Отзыв')

    def __str__(self):
        return str(self.stars)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

# еще мадель отзыв