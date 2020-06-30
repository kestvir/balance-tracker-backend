from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('transaction-list/', views.transactionList, name="transaction-list"),
    path('transaction-detail/<str:pk>/',
         views.transactionDetail, name="transaction-detail"),
    path('transaction-create/', views.transactionCreate, name="transaction-create"),
    path('transaction-update/<str:pk>/',
         views.transactionUpdate, name="transaction-update"),
    path('transaction-delete/<str:pk>/',
         views.transactionDelete, name="transaction-delete"),
]
