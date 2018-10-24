from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.school_list),
    path('list/<int:pk>/', views.school_detail),

]
