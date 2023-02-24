
from django.contrib import admin
from django.urls import path,include
from account.views import home

urlpatterns = [

    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
]
