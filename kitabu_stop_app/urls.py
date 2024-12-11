from django.contrib import admin
from django.urls import path
from kitabu_stop_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('shop/', views.shop, name='shop'),
    path('resources', views.resources, name='resources'),
    path('about/', views.about, name='about'),
    path('', views.register, name='register'),
    path('working/', views.working, name='working'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('product/<int:pk>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('payment/' ,views.payment, name='payment'),
    path('upload_resources/' ,views.upload_resources, name='upload'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('delete_resource/<int:id>/', views.delete_resource, name='delete_resource'),

    
]
