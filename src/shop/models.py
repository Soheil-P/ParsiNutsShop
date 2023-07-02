from django.db import models
from django.urls import reverse

from accounts.models import User

# Create your models here.
class City(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("city-list-page")
    


class Category(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField( max_length=100)
    price=models.DecimalField(decimal_places=3,max_digits=18)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/products')

    def __str__(self):
        return self.title


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    tel=models.CharField(max_length=100)
    city=models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InventoryStock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stocked_quantity = models.DecimalField(decimal_places=3,max_digits=18)
    inventory=models.ForeignKey(Inventory,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} - {self.inventory.name}'


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.get_fullname
    
    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'


class Invoice(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    isPaid=models.BooleanField()
    total_price=models.DecimalField(decimal_places=3,max_digits=18)
    buy_date=models.DateTimeField()

    # def calculate_total_price(self,invoiceitems):
    #     total_amount = 0
    #     for invoice_item in invoiceitems.all():
    #         total_amount += invoice_item.price

    #     return total_amount

    def __str__(self):
        return f'{self.customer.get_fullname} {self.buy_date}'
    

class InvoiceItems(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    quantity=models.DecimalField(decimal_places=3,max_digits=18)
    inventory_stock=models.ForeignKey(InventoryStock,on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=3,max_digits=18)

    def get_price_by_quantity(self):
        return self.inventory_stock.product.price*self.quantity

    def __str__(self):
        return f'product: {self.inventory_stock.product.title} inventory: {self.inventory_stock.inventory.name} quantity: {self.quantity}'
    
    
