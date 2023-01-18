from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.test, name='index'),
    path('menu/',views.MenuItemsView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItem.as_view()),
    path('api-token-auth/',obtain_auth_token),
    
    
]