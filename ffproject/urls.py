from django.contrib import admin
from django.urls import path, include
from apps.users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.helloworld.urls'), name='hello'),
    path('login/', users_view.SiteLoginView.as_view(), name='login'),
    path('profile/', users_view.EditProfileView.as_view(), name='profile'),
]
