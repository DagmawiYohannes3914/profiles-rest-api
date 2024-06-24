from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HellowViewSet

router = DefaultRouter()
router.register('hello-viewset', HellowViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls))
]
