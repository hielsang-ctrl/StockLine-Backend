from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, F
from django.utils import timezone
from datetime import timedelta
from orders.models import Order, OrderItem
from products.models import Product, Category
from products.permissions import IsAdminRole


class DashboardStatsView(APIView):
    permission_classes = [IsAdminRole]

    def get(self, request):
        # Summary cards
        total_products = Product.objects.count()
        total_supplied = Product.objects.aggregate(s=Sum('stock'))['s'] or 0
        total_orders = Order.objects.count()
        pending_orders = Order.objects.filter(status='pending').count()
        shipped_orders = Order.objects.filter(status='shipped').count()
        cancelled_orders = Order.objects.filter(status='cancelled').count()

        # Total units sold & revenue
        sold_data = OrderItem.objects.aggregate(
            units=Sum('quantity'),
            revenue=Sum(F('quantity') * F('unit_price'))
        )
        total_sold = sold_data['units'] or 0
        total_revenue = sold_data['revenue'] or 0

        # Sales by category
        sales_by_category = (
            OrderItem.objects
            .values(cat_name=F('product__category__name'))
            .annotate(units_sold=Sum('quantity'), revenue=Sum(F('quantity') * F('unit_price')))
            .order_by('-units_sold')
        )

        # Stock by category (supplied)
        stock_by_category = (
            Product.objects
            .values(cat_name=F('category__name'))
            .annotate(total_stock=Sum('stock'), product_count=Count('id'))
            .order_by('cat_name')
        )

        # Weekly activity — last 7 days orders
        today = timezone.now().date()
        weekly = []
        for i in range(6, -1, -1):
            day = today - timedelta(days=i)
            count = Order.objects.filter(created_at__date=day).count()
            units = OrderItem.objects.filter(order__created_at__date=day).aggregate(s=Sum('quantity'))['s'] or 0
            weekly.append({'day': day.strftime('%a'), 'orders': count, 'units_sold': units})

        # Top selling products
        top_products = (
            OrderItem.objects
            .values(prod_name=F('product__name'), sku=F('product__sku'))
            .annotate(units_sold=Sum('quantity'), revenue=Sum(F('quantity') * F('unit_price')))
            .order_by('-units_sold')[:5]
        )

        # Recent orders
        recent_orders = Order.objects.select_related('user').order_by('-created_at')[:5]
        recent = [
            {
                'id': o.id,
                'customer': o.user.email,
                'status': o.status,
                'items': o.items.count(),
                'created_at': o.created_at,
            }
            for o in recent_orders
        ]

        return Response({
            'summary': {
                'total_products': total_products,
                'total_supplied': total_supplied,
                'total_sold': total_sold,
                'total_revenue': float(total_revenue),
                'total_orders': total_orders,
                'pending_orders': pending_orders,
                'shipped_orders': shipped_orders,
                'cancelled_orders': cancelled_orders,
            },
            'sales_by_category': list(sales_by_category),
            'stock_by_category': list(stock_by_category),
            'weekly_activity': weekly,
            'top_products': list(top_products),
            'recent_orders': recent,
        })
