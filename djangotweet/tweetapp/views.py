from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.decorators.cache import cache_control
# Create your views here.
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets_1":all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login") 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)           
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
        # tweet = models.Tweet(nickname, message)
        #tweet.save()
        models.Tweet.objects.create(username=request.user, message = message)
        return redirect(reverse("tweetapp:listtweet"))
    else:
        return render(request, "tweetapp/addtweet.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
	del request.session["uid"]
	return redirect('login')

@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:listtweet")   
# def addtweetbyform(request):
#     if request.method == "POST":
#         print(request.POST)
#     else:
#         return render("tweetapp/addtweetbyform.html")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


