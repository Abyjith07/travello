from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    #path('about/',views.about,name='about'),
   # path('contract/',views.contract,name='contract'),
    #path('details/',views.details,name='details'),
    #path('thanks/',views.thanks,name='thanks')

    #path('add/',views.addition,name='addition')
]