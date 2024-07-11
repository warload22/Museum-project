from django.db import models

# Create your models here.
from authapp.models import User
from mainapp.models import Exhibits


class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Exhibits,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'


    def get_basket(self):
        return Basket.objects.filter(user=self.user)

    def total_quantity(self):
        baskets = self.get_basket()
        return sum(basket.quantity for basket in baskets)
