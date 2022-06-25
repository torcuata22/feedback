from django.http import HttpResponseRedirect
from django.shortcuts import render

#from feedback import reviews
from .forms import ReviewForm 
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Review #(with a ModelForm I don't need the Review instance, but I'm importing it for the TemplateView so I can access th reviews and display them)
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

# Create your views here.
#in this case, get() and post() are dedicated methods from django that automatically detect which requet is which
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        fav_review = Review.objects.get(ph=review_id)
        request.session["favorite_review"]=fav_review #stores new information

class ReviewView (CreateView):
    model = Review
    form_class = ReviewForm #so I can customize what I want
    #fields = "__all__"  takes all the fields from the model mentioned above, BUT it doesn't allow to customize
    #form_class = ReviewForm Necesary for FormView, but not for CreateView
    template_name = "reviews/review.html"
    success_url = "/thank_you"
    
    #I don't need it because I'm working with CreateView
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    
    #Django takes care of these now:
    # def get(self,request):
    #     form = ReviewForm()  
    #     return render(request, "reviews/review.html", {
    #     "form": form 
    # } )
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank_you")
    #     return render(request, "reviews/review.html", {
    #     "form": form 
    # } )
    
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


class ReviewsListView(ListView):
    template_name= "reviews/review_list.html"
    model = Review #points at class but doesn't instantiate it
    context_object_name = "reviews"
    
    #If I wanted to filter based on rating:
    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
   
    
class SingleReviewView(DetailView):
    template_name= "reviews/single_review.html"
    model = Review
    
     
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) #remember: this is a dictionary
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"]= selected_review
    #     return context
    
        
    
  
#def thank_you (request):
    #return render(request, "reviews/thank_you.html" )