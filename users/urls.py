from django.urls import path

from users.views import UsersView, UsersDetailView, UsersMeView
urlpatterns = [
    path('', UsersView.as_view()),
    path('me/', UsersMeView.as_view()),
    path('<int:pk>/', UsersDetailView.as_view())
]
