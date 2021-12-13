
from django.urls import path
from .views import RegisterUser, MyTokenObtainPairView, TokenRefreshView, ApiRoot, Success
from rest_framework.urlpatterns import format_suffix_patterns


app_name='account'
urlpatterns = format_suffix_patterns([
    path('', ApiRoot.as_view(), name='root'),
    path('success', Success.as_view(), name='success'),
    path('registration/', RegisterUser.as_view(), name='user-registration'),
    path('api/token', MyTokenObtainPairView.as_view(), name='token-obtain'),
    path('api/refresh', TokenRefreshView.as_view(), name='token-refresh'),
])

