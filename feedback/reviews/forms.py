from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name"
#     })
#     review_text = forms.CharField(label= "Your Feedback", widget=forms.Textarea, max_length=200)
#     rating=forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  #this is a special identifier that adds all the fields
        #if I don't want all the fields to show to user, create a list of fields to be included in the form, for example: fields = ['review_text', 'rating'] 
        