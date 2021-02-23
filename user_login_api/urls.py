from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registration.urls')),
    path('products/',include('Product.urls')),
    path('movies/',include('Movie_cbv.urls')),
    path('gamestore/',include('Gamestore_gcbv.urls')),
    path('employee/',include('Employee_auth.urls')),
    path('drf_docs_app/',include('drf_docs_app.urls'))
]
