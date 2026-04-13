from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:analysis_id>/', views.result, name='result'),
    path('loading/<int:analysis_id>/', views.loading, name='loading'),
    path('status/<int:analysis_id>/', views.status, name='status'),
    path('history/', views.history, name='history'),
]