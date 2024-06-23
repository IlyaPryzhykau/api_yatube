from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import include, path

from .views import GroupViewSet, UserViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='post-comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
