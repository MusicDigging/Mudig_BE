"""
URL configuration for mudig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

from django.contrib.auth.decorators import login_required

from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularYAMLAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('playlist/', include('playlist.urls')),
    
    # Open API 자체를 조회 : json, yaml
    # path("api/json/", login_required(SpectacularJSONAPIView.as_view()), name="schema-json"), # 로그인을 해야만 볼 수 있음.
    
    path("api/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("api/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    # Open API Document UI로 조회: Swagger, Redoc
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui",),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc-ui",),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
