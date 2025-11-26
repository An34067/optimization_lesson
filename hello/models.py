from django.db import models

# Create your models here.

# class Authors(models.Model):
#     name = models.CharField("Имя", max_length=30)

#     class Meta:
#         verbose_name = "Автор"
#         verbose_name_plural = "Авторы"
    
#     def __str__(self):
#         return f"{self.name}"
    
# class Publication_house(models.Model):
#     name = models.CharField()

#     class Meta:
#         verbose_name = "Издательство"
#         verbose_name_plural = "Издательства"

#     def __str__(self):
#         return f"{self.name}"

# class Book(models.Model):
#     title = models.CharField("Название")
#     authors = models.ManyToManyField(Authors, verbose_name='Авторы')
#     publication_house = models.ForeignKey(Publication_house, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = "Книга"
#         verbose_name_plural = "Книги"

#     def __str__(self):
#         return self.title
    
class Manufacturer(models.Model):
    name = models.CharField()

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return f"{self.name}"

class Item(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.price})'