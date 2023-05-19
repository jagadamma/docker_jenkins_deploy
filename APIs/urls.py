from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('create/', views.add_jds, name='add-jd'),
    path('all/', views.view_items, name='view_items'),
]
