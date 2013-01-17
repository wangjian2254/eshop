#coding=utf-8
'''
Created on 2011-6-15

@author: 王健
'''
from django.contrib import admin
from shop.models import Person, Address, Kind, ProductInfo, Product, ProductImg, Order, OrderProduct, Tags, Eshop, Ad, ProductPreference, Preferences, OrderProductProd


admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Kind)
admin.site.register(Tags)
admin.site.register(ProductInfo)
admin.site.register(Product)
admin.site.register(ProductImg)
admin.site.register(ProductPreference)
admin.site.register(Preferences)
admin.site.register(OrderProduct)
admin.site.register(OrderProductProd)
admin.site.register(Order)
admin.site.register(Eshop)
admin.site.register(Ad)