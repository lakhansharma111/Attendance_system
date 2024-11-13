from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import RegisterUserView, ObtainAuthTokenView
from roster.views import StaffViewSet, ShiftViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/token/', ObtainAuthTokenView.as_view(), name='token_obtain_pair'),
    path('api/', include(router.urls)),
]
