from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('',views.teamfn,name='teamfn')

    #path('add/',views.addition,name='addition')
]