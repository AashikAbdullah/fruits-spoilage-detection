from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('index/', views.index, name='index'),
    path('problem_statement/', views.problem_statement, name='problem_statement'),
    # path('company_info/', views.company_information,name='company_info'),
    # path('company_database/', views.company_database, name='company_database'),
    path('model/', views.model, name='model'),
    path('model1/', views.model1, name='model1'),
    path('model_database/', views.model_database, name='model_database'),

]
