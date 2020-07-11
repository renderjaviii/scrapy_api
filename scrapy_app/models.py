from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=100)
    created_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return "id: {}, name: {}".format(self.id, self.name)
