
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/HappyMarineShipping/',include("api.HappyMarineShipping.urls"))
]


urlpatterns += staticfiles_urlpatterns()

