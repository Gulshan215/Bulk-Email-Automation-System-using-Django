from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tempalte_list, name="home"),
    path('template_edit/<int:pk>',views.template_edit,name="template_edit")
]

