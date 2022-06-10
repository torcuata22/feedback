from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm 

# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
         
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank_you")   # redirects to new page, creating GET request instead of another from method=POST
        

    form = ReviewForm()        
    return render(request, "reviews/review.html", {
       "form": form 
    } )
    
  
def thank_you (request):
    return render(request, "reviews/thank_you.html" )