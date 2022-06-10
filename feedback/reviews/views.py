from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm 

# Create your views here.

def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST["username"] #extracts incoming data
    #     print(entered_username)                     #prints incoming data
    #     return HttpResponseRedirect("/thank_you")   # redirects to new page, creating GET request instead of another from method=POST
        

    form = ReviewForm()        
    return render(request, "reviews/review.html", {
       "form": form 
    } )
    
  
def thank_you (request):
    return render(request, "reviews/thank_you.html" )