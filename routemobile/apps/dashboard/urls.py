from django.urls import path
from .views import ItemsView

urlpatterns = [
    path('additem',ItemsView.as_view()),
]
