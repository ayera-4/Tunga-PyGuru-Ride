from django.db import models

# Create your models here
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_quantity = models.FloatField(blank=True)
    item_price = models.FloatField(blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.item_name