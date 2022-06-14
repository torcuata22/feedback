from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm 
#from .models import Review (because with a ModelForm I don't need the Review instance)

# Create your views here.

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
         
        if form.is_valid(): #If I'm using ModelForm, I can skip all this (no need to create model instance):
            # review = Review(user_name = form.cleaned_data['user_name'], 
            #                 review_text=form.cleaned_data['review_text'], 
            #                 rating=form.cleaned_data['rating']) 
            #review.save() #all this only happens if user entered valid data
            form.save() #I can just call save on the form because it's a model form
            return HttpResponseRedirect("/thank_you")   # redirects to new page, creating GET request instead of another from method=POST
    
    else:
        form = ReviewForm()  
              
    return render(request, "reviews/review.html", {
       "form": form 
    } )
    
  
def thank_you (request):
    return render(request, "reviews/thank_you.html" )