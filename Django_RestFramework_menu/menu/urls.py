from django.urls import path
from .views import *
urlpatterns = [
    path('',item_list),
    path('drf/',item_list_serialized),
    path('drf/<int:pk>',item_detail),
    # path('admin/', admin.site.urls),
    # path('menu/',include('menu.urls')),
]