from django.urls import path,include
from .import views
urlpatterns = [
     # path('login/', views.login, name='login'),
     path('amount/', views.amount, name="amount"),
     path('journal_entry_list/', views.journal_entry_list, name="journal_entry_list"),
     path("accounts/", include("django.contrib.auth.urls")),
]