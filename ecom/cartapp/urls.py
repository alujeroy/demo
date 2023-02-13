from django.urls import path
from .import views
app_name='cartapp'


urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('del/<int:product_id>/',views.del_cart,name='del_cart'),
    path('remove/<int:product_id>/', views.remove, name='remove')

]