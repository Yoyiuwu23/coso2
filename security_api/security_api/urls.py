from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Security API",
      default_version='v1',
      description="Documentación de la API de seguridad",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@securityapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]