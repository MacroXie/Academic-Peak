# the urls.py for translator
from django.urls import path
from translator import views

urlpatterns = [
    path('', views.index, name='Translator'),
    path('api/', views.translate, name='translate_api'),
]