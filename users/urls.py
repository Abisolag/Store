from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.create_user, name='signup'),
    path('account/profile/', views.profile, name='profile'),
    path('account/profile_update/', views.profile_update, name='profile_update'),
    

]