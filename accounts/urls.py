from django.urls import path
from . import views
import newsBigdata.views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', newsBigdata.views.index, name='index'), ##먼가 위치가 이상함....
]