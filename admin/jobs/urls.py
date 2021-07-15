from django.urls import path

from .views import JobViewSet, UserAPIView

urlpatterns = [
    path('jobs', JobViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('jobs/<str:pk>', JobViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]