
from django.urls import path, include
from . import views
app_name = 'taskapp'
urlpatterns = [

    path('',views.home,name='home'),
    # path('detail',views.detail,name="detail")
    path('del/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.classviews.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.classdetail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.classupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.classdelete.as_view(),name='cbvdelete')
]
