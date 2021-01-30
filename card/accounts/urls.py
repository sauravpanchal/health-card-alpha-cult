from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_admin),

    path('register/', views.register, name="register"),   
    path('login_admin/', views.login_admin, name="login"),
    path('logout_admin/', views.logout_admin, name="logout"),

    path('user_admin/', views.user_admin, name="user_admin"),
    path('user_viewer/', views.user_viewer),  

    path('create_user/', views.create_user, name="create_user"),
    path('update_user/<str:pk_test>/', views.update_user, name="update_user"),
    path('delete_user/<str:pk_test>/', views.delete_user, name="delete_user"),

]
