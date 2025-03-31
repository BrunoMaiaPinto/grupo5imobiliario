from django.urls import path
from . import views


app_name = 'radarimovel'
urlpatterns = [
  path('index', views.index, name='index'),
  path('login',views.user_login,  name='login'),
  path('consulta', views.imoveis, name='consulta'),
  # path('consulta', views.proprietarios, name='consulta'),
  path('inserir', views.inserir, name='inserir'),]
