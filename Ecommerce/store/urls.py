from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('cheekout/', views.cheekout, name="cheekout"),
	path('update_Item/', views.updateItem, name="update_Item"),
	path('bikeview/', views.bikeview, name="bikeview"),
	path('ServiceBike/', views.ServiceBike, name="ServiceBike"),



]
