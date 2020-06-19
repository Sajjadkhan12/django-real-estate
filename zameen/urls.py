
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shelter.urls')),
    path('agents/',include('agents.urls')),
    # path('account/',include('users.urls')),
]

