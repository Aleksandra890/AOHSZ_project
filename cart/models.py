from django.db import models



class Cart (models.Model):
    catProf = models.CharField('Заказчик', max_length=50, default='admin')
    nameCart = models.CharField('Название', max_length=200)
    imageCart = models.ImageField(upload_to='catalog/', blank = True)
    textCart = models.TextField('Краткое описание')
    metka = models.BooleanField('Гражданский', default=True)
    

    def __str__(self):
        return self.nameCart 
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'