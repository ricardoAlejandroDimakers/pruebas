from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kmsapp'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^formulario/$', views.Formulario, name='formulario')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)