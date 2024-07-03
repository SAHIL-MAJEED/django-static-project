from django.shortcuts import render


# Create your views here.
def my_view(request):
    myname="sahil"
    favplayer="markwood"
    favanimal="woont"
    favsubject="tanveer ul ainaain"
    d={"name":myname,"Player":favplayer,"animal":favanimal,"subject":favsubject}
    return render(request,"myapp/1.html",d)