from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (confirmAttendanceAPIView, EventListCreateAPIView,
                    ReviewserializerAPIView, ReviewserializerDetailView)

router=DefaultRouter()
router.register("",EventListCreateAPIView,base_name='events')
# router.register("reviews",ReviewserializerDetailView,base_name="reviews")
router.register("confirm-attendance",confirmAttendanceAPIView)


urlpatterns = [
    path("",include(router.urls)),
    path("<int:event_pk>/reviews/",ReviewserializerAPIView.as_view(),name="event_reviews"),
    path('reviews/<int:pk>/',ReviewserializerDetailView.as_view(),name='review-details')
]
