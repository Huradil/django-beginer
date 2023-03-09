from django.db import models

class TestModel(models.Model):
    string=models.CharField(max_length=20,verbose_name="Название поля 1")
    date=models.DateField(verbose_name="дата 1")
    datetime=models.DateTimeField(verbose_name="дата и время")
    checkbox=models.BooleanField(verbose_name="чек бокс")
    interger=models.IntegerField(verbose_name="число")
    choces=models.IntegerField(verbose_name="выборка",choices=(
        (1,'one'),
        (2,'two'),
        (3,'three'),
    ))
    nullable=models.TextField(verbose_name="какой то текст",blank=True,null=True)

    def __str__(self):
        return f'Тестова модель №{self.id}'