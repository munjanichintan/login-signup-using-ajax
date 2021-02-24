"""signuplogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.UserView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('retrieve/<int:pk>', views.RetrieveView.as_view(), name='retrieve'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('loginhtml/', views.login, name='loginhtml'),
    path('signuphtml/', views.signup, name='signuphtml'),
    path('retrievehtml/', views.retrieve, name='retrievehtml'),
    path('updatehtml/', views.update, name='updatehtml'),
    path('deletehtml/', views.delete, name='deletehtml'),
    path('success/', views.success, name='success'),
    path('forgothtml/', views.forgot, name='forgothtml'),

    path('home/', views.home),

]
