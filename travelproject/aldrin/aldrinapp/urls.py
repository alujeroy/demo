from . import views
from django.urls import path, include

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('res/',views.res,name='res')
#     path('', views.add, name='add')
]
