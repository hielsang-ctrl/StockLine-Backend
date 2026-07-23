from django.urls import path
from .views import OrderListCreateView, OrderDetailView
from .dashboard import DashboardStatsView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
]
