from django.shortcuts import render
from .models import Home,About,Gallery,Exhibition,Social_Profile

# Create your views here.
def home(request):

    home = Home.objects.latest('id')

    about = About.objects.latest('id')

    gallery = Gallery.objects.all()

    exhibition = Exhibition.objects.all()

    social_profile = Social_Profile.objects.all()
    

    context = {
        'home':home,
        'about':about,
        'gallery':gallery,
        'exhibition':exhibition,
        'social_profile':social_profile,
    }


    return render(request, 'index.html',context)