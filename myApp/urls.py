"""
URL configuration for myProject project.

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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index2, name='index2'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('uploadata', views.uploadata, name='uploadata'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('customers', views.customers, name='customers'),
    path('bills', views.bills, name='bills'),
    path('reports', views.reports, name='reports'),
    path('adduser', views.adduser, name='adduser'),
    path('deletedata/<int:id>', views.deletedata, name='deletedata'),
    path('viewdata/<int:id>', views.viewdata, name='viewdata'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('bills2', views.bills2, name='bills2'),
    path('uploapayment', views.uploapayment, name='uploapayment'),
    path('upload_image/', views.upload_image, name='upload_image'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)