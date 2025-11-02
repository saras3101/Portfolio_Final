from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
]