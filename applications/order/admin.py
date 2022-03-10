from django.contrib import admin

from applications.order.models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1
    fields = ('product', 'quantity', 'total_cost')


class OrderAdminDisplay(admin.ModelAdmin):
    inlines = [OrderProductInline, ]


admin.site.register(Order, OrderAdminDisplay)
