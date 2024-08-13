from . import views     
from django.urls import path

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name = 'listtweet'), # atilsamancıoğlu.com/tweetapp/
    path('addtweet/', views.addtweet, name= "addtweet"), # atilsamancioglu.com/tweetapp/addtweet
    path('listtweet/', views.listtweet, name= "listtweet"), # atilsamancioglu.com/tweetapp/addtweet  #bu satıtrı sil duruma göre
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.deletetweet, name="deletetweet")
]
