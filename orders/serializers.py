from rest_framework import serializers
from django.db import transaction
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    sku = serializers.CharField(source='product.sku', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'sku', 'quantity', 'unit_price')
        read_only_fields = ('unit_price',)


class OrderCreateSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.DictField(), min_length=1, write_only=True
    )

    def validate_items(self, items):
        validated = []
        for entry in items:
            try:
                product = Product.objects.get(id=entry['product_id'])
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Product {entry['product_id']} not found.")
            qty = int(entry.get('quantity', 1))
            if qty < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")
            if product.stock < qty:
                raise serializers.ValidationError(f"Insufficient stock for '{product.name}'.")
            validated.append({'product': product, 'quantity': qty})
        return validated

    @transaction.atomic
    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.create(user=user)
        for entry in validated_data['items']:
            product = entry['product']
            qty = entry['quantity']
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                unit_price=product.price,
            )
            product.stock -= qty
            product.save(update_fields=['stock'])
        return order


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'created_at', 'updated_at', 'items')
        read_only_fields = ('created_at', 'updated_at')
