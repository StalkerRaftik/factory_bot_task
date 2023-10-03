from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


paths = [
    path('api/', include(f'apps.{URLS_PATH}.urls'))
    for URLS_PATH in settings.PROJECT_APPS
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/endpoint/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    *paths,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
