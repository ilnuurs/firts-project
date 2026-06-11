from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(verbose_name="Изображение", upload_to="categories/")
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=200,  verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    info = models.TextField(verbose_name='Информация')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name='products', verbose_name='Категория')
    image = models.ImageField(verbose_name="Изображение", upload_to="products/", null=True, blank=True)  
    created_at = models.DateField(verbose_name="Создано в", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата обновление", auto_now=True)
    
    def __str__(self):
        return f'{self.name} - coin{self.price}'

    