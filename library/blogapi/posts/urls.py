from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet,UserViewSet
# from .views import PostListAPIView,PostDetailAPIView,UserListAPIView,UserDetailAPIView
# urlpatterns = [
    # path('', PostListAPIView.as_view(), name='post-list'),
    # path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    # path('user/', UserListAPIView.as_view(), name='user-list'),
    # path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
# ]
router = SimpleRouter()
router.register('posts',PostViewSet,basename='posts')
router.register('users',UserViewSet,basename='users')
urlpatterns = router.urls