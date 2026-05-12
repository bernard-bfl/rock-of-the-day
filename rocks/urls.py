from django.urls import path 
from .views import RockListView, RockDetailView, RockOfTheDayView


urlpatterns = [
    path('rocks/', RockListView.as_view(), name='rock-list'),
    path('rocks/today/', RockOfTheDayView.as_view(), name='rock-of-the-day'),
    path('rocks/<int:pk>/', RockDetailView.as_view(), name='rock-detail'),
]