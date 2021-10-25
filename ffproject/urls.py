from django.contrib import admin
from django.urls import path, include
from apps.users import views as users_view
from apps.feed import views as feed_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.helloworld.urls'), name='hello'),

    path('login/', users_view.SiteLoginView.as_view(), name='login'),
    path('profile/', users_view.ProfileEditView.as_view(), name='profile'),
    path('register/', users_view.SiteRegisterView.as_view(), name='register'),
    path('register/success/', users_view.SiteRegisterViewSuccess.as_view(), name='register_success'),
    path('logout/', users_view.SiteLogoutView.as_view(), name='logout'),

    path('post/', feed_view.show_post, name='show_post'),
    path('post/new/', feed_view.create_post, name='create_post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
