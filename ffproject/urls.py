from django.contrib import admin
from django.urls import path, include
from apps.users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.helloworld.urls'), name='hello'),
    path('login/', users_view.SiteLoginView.as_view(), name='login'),
    path('profile/', users_view.EditProfileView.as_view(), name='profile'),
    path('register/', users_view.SiteRegisterView.as_view(), name='register'),
    path('register/ok/', users_view.SiteRegisterViewOk.as_view(), name='register_ok'),
    path('logout/', users_view.SiteLogoutView.as_view(), name='logout'),
]
