from django.urls import path
from ishu import views

# localhost:8000/ishu
urlpatterns = [
    path('',views.ishuapp,name='ishuapp'),
    path('<int:drink_id>/',views.drink_detail,name='drink_detail'),
    path('storeview/',views.store_view,name='storeview'),
]