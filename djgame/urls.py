"""
URL configuration for djgame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from backend.views import*
from frontend.views import*
from frontend.views import Blogpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("message/",msg),
    path("forms/",form,name="form"),
    path("save/",save,name="save"),
    path("table/",table),
    path("delete/<int:dataid>/",delete,name="delete"),
    path("edit/<int:dataid>/",edit,name="edit"),
    path('',Index,name="Index"),
    path("Gallery/",Gallery,name="Gallery"),
    path("About/",About,name="About"),
    path("Services/",Services,name="Services"),
    path("Blog/",Blog,name="Blog"),
    path('Blog/', Blogpage, name='Blog'),

]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)