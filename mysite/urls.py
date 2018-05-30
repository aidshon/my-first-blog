from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^example/', include('example.urls')),
    url(r'^bliss/', include('bliss.urls')),
]
