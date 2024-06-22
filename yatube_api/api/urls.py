from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import include, path

from .views import GroupViewSet, UserViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='post-comments')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
