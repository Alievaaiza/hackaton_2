from rest_framework import serializers

from applications.order.models import OrderProduct, Order


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity', 'total_cost')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderProductSerializer(many=True, write_only=True, required=True)
    total_cost = serializers.DecimalField(max_digits=100, decimal_places=2, default=1)
    delivery_address = serializers.CharField(max_length=255, required=True)
    contact_number = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Order
        fields = (
            'items', 'total_cost',
            'delivery_address', 'contact_number',
            'first_name', 'status'
        )

    def create(self, validated_data):
        # {'items': [
        # OrderedDict([('product', < Product: product1 >), ('quantity', 5)]),
        # OrderedDict([('product', < Product: product2 >), ('quantity', 3)])], 'total_cost': 1,
        # 'delivery_address': 'Bishkek', 'contact_number': '+996555333222', 'first_name': 'Tom'}
        request = self.context.get('request')
        items = validated_data.pop('items')
        if request.user.is_authenticated:
            validated_data['user_id'] = request.user.id
        order = Order.objects.create(**validated_data)
        total_order_cost = 0
        for item in items:
            product = item['product']
            order_product = OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )
            total_order_cost += order_product.total_cost
        order.total_cost = total_order_cost
        order.save()
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['products'] = OrderProductSerializer(OrderProduct.objects.filter(order=instance.id), many=True).data
        return rep
