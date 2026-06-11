"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import main, about,  product_detail, contacts, list1, students, product_create, product_delete,product_update   
urlpatterns = [
    path("", main, name="main"),
    path('index/',main),
    path("about/", about),
    path('contacts/',contacts),
    path('admin/', admin.site.urls),
    path("list/",list1),
    path("students/",students),
    
    # <----- CRUD PRODUCTS ----->
    path('product-create/',product_create, name="product_create" ),
    path('product-detail/<int:id>/', product_detail, name='product_detail'),
    path("product-delete/<int:pk>/", product_delete, name="product_delete"),
    path('product-update/<int:id>/', product_update, name="product_update")
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    