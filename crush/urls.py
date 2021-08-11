from django.urls import path,re_path
from crush import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('create/',views.CreateUserView.as_view(),name='create_user'),
    re_path('detail/(?P<pk>\d+)/',views.UserDeatilView.as_view(),name='user_detail'),
    path('calculate/<num>/',views.calculate,name='calculate'),
    re_path('pranked/(?P<pk>\d+)/',views.FooledView.as_view(),name='fooled'),
]
