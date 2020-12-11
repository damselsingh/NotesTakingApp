from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.user_signup, name="signup"),
    path('dashboard/', views.user_notes, name="notes"),
    path('logout/', views.user_logout, name="logout"),
    path('insert-your-notes/', views.take_notes, name="takenotes"),
    path('your-notes/', views.your_notes, name="yournotes"),
    path('setting/', views.user_setting, name="setting"),
    path('delete/<int:pk>/', views.data_delete, name="delete"),
    path('update/<int:pk>/', views.data_update, name="update"),
    path('views/<int:pk>/', views.data_views, name="view"),
]
