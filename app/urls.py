from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
	path('',views.home,name="home"),
    path('preview/',views.preview,name="preview"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.register,name="register_url"),
    path('logout',LogoutView.as_view(next_page='preview'),name="logout"),
]