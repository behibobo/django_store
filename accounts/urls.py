from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView

# router=DefaultRouter()

# router.register("all-profiles",UserProfileListCreateView)
# router.register("profile/<int:pk>",userProfileDetailView,basename='profile')

urlpatterns = [
    path("profiles",UserProfileListCreateView.as_view(),name="profiles"),
    path("profiles/<int:pk>",userProfileDetailView.as_view(),name="profile")
    # path("",include(router.urls))
]
