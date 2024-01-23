from django.urls import path
from . import views


urlpatterns = [
    path('bank/', views.bank_create, name='bank_create'),
    path('bank/<int:pk>/update/', views.bank_update, name='bank_update'),
    path('bank/<int:pk>/delete/', views.bank_delete, name='bank_delete'),
    path('bank/list/', views.bank_list, name='bank_list'),
]



