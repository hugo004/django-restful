"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from todo import views

schema_view = get_schema_view(
   openapi.Info(
      title="Django Demo API",
      default_version='v1',
      description="Test description"
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router =  routers.SimpleRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

modules =[
    path('', include(router.urls))
]


urlpatterns += modules