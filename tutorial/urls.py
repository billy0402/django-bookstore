from django.urls import path

from . import views

urlpatterns = [
    path('', views.root),
    path('hello/<str:name>/', views.hello),
    path('square/<int:number>/', views.square),
    path('sequence/<int:number1>/<int:number2>/', views.sequence),
]
