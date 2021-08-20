
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(the url,function,nameofpath)
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),

]
