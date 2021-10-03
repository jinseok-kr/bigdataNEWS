from django.urls import include, path
from . import views
import newsBigdata.views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ##먼가 위치가 이상함....
]