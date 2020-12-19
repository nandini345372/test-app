from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name="create"),
    path('display/',views.displayBlog,name="display"),
    path('update/<id>',views.updatelist,name="update"),
    path('delete/<id>',views.deletelist,name="delete"),

]