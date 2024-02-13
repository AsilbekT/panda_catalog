"""
URL configuration for catalog_service project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Panda Streaming Platform Administration"
admin.site.site_title = "Panda Admin Portal"
admin.site.index_title = "Welcome to Panda Streaming Platform Admin"


urlpatterns = [
    path('catalogservice/admin/', admin.site.urls),
    path('catalogservice/', include('video_api.urls')),
    path('catalogservice/', include('video_app.urls')),
    path('catalogservice/', include('video_search.urls')),
    path('catalogservice/management/', include('catalog_management_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
