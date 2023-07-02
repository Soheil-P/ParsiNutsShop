from django.contrib import admin

from shop.models import Category, City, Customer, Inventory, InventoryStock, Invoice, InvoiceItems, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(InventoryStock)
admin.site.register(Inventory)
admin.site.register(City)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItems)
