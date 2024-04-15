from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core import views
from core.auth import CustomObtainAuthToken
from help_prav_server import settings

router = routers.DefaultRouter()
router.register(r"news", views.NewsViewSet)
router.register(r"employe", views.EmployesViewSet)
router.register(r"cart", views.ShopViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/wallet/", views.WalletView.as_view()),
    path("api/profile/", views.UserProfileView.as_view()),
    path('login/', CustomObtainAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
