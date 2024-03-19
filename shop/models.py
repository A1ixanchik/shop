from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.name}  - {self.price}'


class Clients(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=10)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    date_purchased = models.DateField()

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return f'{self.name}  - {self.age}'



