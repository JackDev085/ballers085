from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render 
def custom_404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ballers085.urls')),
]


handler404 = custom_404
