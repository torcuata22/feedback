from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile



# Create your views here.
#helper finction:
#def store_file(file):
    #with open("temp/image.jpg", "wb+") as dest:
        #for chunk in file.chunks():
            #dest.write(chunk)
#not needed anymore because I'm using model


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
    #by ising this, validation and get/post is taken care of by Django
    
class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html" 
    context_object_name = "profiles"

        

    
    
        
    '''
    This is not needed anymore because I'm now using CreateView
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_form=ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            #store_file(request.FILES["image"]) will substitute for model
            profile = UserProfile(image=request.FILES["user_image"]) #user_image because this is the name of the field in the model
            profile.save()
            return HttpResponseRedirect("/profiles")
           
        return render(request, "profiles/create_profile.html", {
            "form":submitted_form
        }) #this added basic validation wihtout us having to write the logic for it
    
        '''