from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,BusinessForm,ProjectForm,BusinessForm,PostForm
from .models import Business,Profile,Project,Post
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

def index(request):
    current_user = request.user
    
    projects = Project.objects.order_by('-date')
    business = Business.objects.all()
    profile = Profile.objects.order_by('-last_update')

    return render(request,'index.html',{"business":business,"profile":profile,"projects":projects})
