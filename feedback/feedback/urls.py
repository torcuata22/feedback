"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from feedback.reviews.views import ReviewsListViews
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", include("reviews.urls")),
    path("",views.ReviewView.as_view()),
    path("thank_you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()),
    path("profiles/", include ("profiles.urls"))
    
]
