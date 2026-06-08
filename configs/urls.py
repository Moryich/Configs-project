from django.urls import path

from configs.views import ConfigsView, ConfigDetailView

urlpatterns = [
    path('', ConfigsView.as_view()),
    path('<int:pk>/', ConfigDetailView.as_view())
]
