from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('pertsonak/', views.pertsonak, name='pertsonak'),
    path('kotxeak/', views.kotxeak, name='kotxeak'),

    path('delpertsona/<int:id>', views.delpertsona, name='delpertsona'),
    path('delkotxea/<int:id>', views.delkotxea, name='delkotxea'),

    path('addpertsona/', views.addpertsona, name='addpertsona'),
    path('addkotxea/', views.addkotxea, name='addkotxea'),

    path('addpertsona/addpertsonatodb/', views.addpertsonatodb, name='addpertsonatodb'),
    path('addkotxea/addkotxeatodb/', views.addkotxeatodb, name='addkotxeatodb'),

    path('updatepertsona/<int:id>', views.updatepertsona, name='updatepertsona'),
    path('updatekotxea/<int:id>', views.updatekotxea, name='updatekotxea'),

    path('updatepertsona/updatepertsonaondb/<int:id>', views.updatepertsonaondb, name='updatepertsonaondb'),
    path('updatekotxea/updatekotxeaondb/<int:id>', views.updatekotxeaondb, name='updatekotxeaondb'),

]