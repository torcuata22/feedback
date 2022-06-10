from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):
    if request.method == 'POST':
        entered_username = request.POST["username"] #extracts incoming data
        print(entered_username)                     #prints incoming data
        return HttpResponseRedirect("/thank_you")   # redirects to new page, creating GET request instead of another from method=POST
        
    return render(request, "reviews/review.html" )
        
    
  
def thank_you (request):
    return render(request, "reviews/thank_you.html" )