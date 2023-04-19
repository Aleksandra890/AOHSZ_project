from django.db import models

class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    image = models.ImageField(upload_to='catalog/', blank = True)
    text1 = models.TextField('Краткое описание')
    text2 = models.TextField('Характеристика2', default='_')
    metka = models.BooleanField('Гражданский', default=True)
    

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Корабль'
        verbose_name_plural = 'Корабли'
