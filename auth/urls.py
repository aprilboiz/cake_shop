from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from auth import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"register", views.RegistrationView, basename="auth_register")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls), name="auth_register"),
]
