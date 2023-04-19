from django.db import models

class New(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField(upload_to='catalog/', blank = True)
    text1 = models.TextField('Анонс')
    fultext = models.TextField('Статья')
    data = models.DateField()

    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return '/news'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class SME(models.Model):
    name = models.CharField('Название', max_length=200)
    imageS = models.ImageField(upload_to='catalog/', blank = True)
    anons = models.CharField('Анонс',max_length=250)
    data1 = models.DateField()
    ss = models.TextField('Ссылка', max_length=450, default='')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'СМИ'
        verbose_name_plural = 'СМИ'

    
