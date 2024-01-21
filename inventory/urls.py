from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('list', views.StockListView.as_view(), name='inventory'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),
    path('audit-stock/', views.audit_stock, name='audit-stock'),
    path('stock/<pk>/read/', views.StockDetailView.as_view(), name='read-stock'),
    path('upload',views.simple_upload,name='upload')
]

