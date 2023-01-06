from . import views

from appliapp import views, api
from django.urls import path
from appliapp import views
urlpatterns = [
     path('',views.home,name='home'),
     path('data', views.dht11, name='Data'),

##api
     path('api/list',api.Dlist, name='DHT11List'),
     path('api/post',api.Dhtviews.as_view(), name='DHT_post'),
     path('tab',views.tab, name='tab'),
     path('alerte/',views.alerte, name='alerte'),
     path('graphe/',views.graphe, name='graphe'),
     path('historique/',views.historique, name='historique'),
     path('export_xls24h', views.export_xls24h, name = 'export_xls24h'),
     path('export_xls48h', views.export_xls48h, name='export_xls48h'),
     path('export_xlsweek', views.export_xlsweek, name='export_xlsweek'),
]
