from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
