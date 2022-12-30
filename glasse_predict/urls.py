from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('predict_price/',include('predict_price.urls')),
]
 