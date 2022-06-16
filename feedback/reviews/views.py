from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm 
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Review #(with a ModelForm I don't need the Review instance, but I'm importing it for the TemplateView so I can access th reviews and display them)

# Create your views here.
#in this case, get() and post() are dedicated methods from django taht automatically detect which requet is which
class ReviewView (View):
    def get(self,request):
        form = ReviewForm()  
        return render(request, "reviews/review.html", {
        "form": form 
    } )
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        return render(request, "reviews/review.html", {
        "form": form 
    } )
    
        '''
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
        '''
        
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context

class ReviewsListViews(TemplateView):
    template_name= "reviews/review_list.html"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        reviews=Review.objects.all()
        context['reviews']=reviews
        return context
        
    
  
#def thank_you (request):
    #return render(request, "reviews/thank_you.html" )