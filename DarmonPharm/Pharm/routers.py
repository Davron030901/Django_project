from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'warehouse_order', views.WarehouseOrderViewSet)
router.register(r'warehouses', views.WarehouseViewSet)

urlpatterns = router.urls
