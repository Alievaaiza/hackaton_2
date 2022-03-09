from rest_framework.routers import DefaultRouter

from applications.review.views import ReviewViewSet


router = DefaultRouter()
router.register('', ReviewViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)