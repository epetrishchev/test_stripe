from django.db import models


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание', max_length=800)
    price = models.FloatField('Цена')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-name', '-price']
