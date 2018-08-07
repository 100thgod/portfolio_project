from django.urls import path
from . import views
urlpatterns = [
    path('',views.detail,name= "detail"),
    path('<int:blog_id>/',views.detailblog,name = "detailblog"),
]