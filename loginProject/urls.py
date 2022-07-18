from django.contrib import admin
from django.urls import path
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    path('login/', views.login, name="login"),

    path('logout/', views.logout, name="logout"),

    path('signup/', views.signup, name='signup'),
]
