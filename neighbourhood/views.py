from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,BusinessForm,ProjectForm,BusinessForm,PostForm
from .models import Business,Profile,Project,Post
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

def index(request):
    current_user = request.user
    projects = Project.objects.all().order_by('-date')
    business = Business.objects.all()
    profile = Profile.objects.order_by('-last_update')

    return render(request,'index.html',{"business":business,"profile":profile,"projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.admin = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request,'new_project.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    #profile = Profile.objects.get(user_id=current_user.id)
    
    return render(request, 'profile.html',{"user":user, "current_user":request.user})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect ('profile')
    else:
        form = ProfileForm()
    
    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    user = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance = user)
        if form.is_valid():
            profile = form.save(commit=False)
            # profile.user = current_user
            profile.save()
        return redirect ('profile')
    else:
        form = ProfileForm(instance = user)
    
    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.hood_admin= current_user
            neighbourhood.save()
        return redirect('home')
    else:
        form = NeighbourhoodForm()
    
    return render(request,'new_hood.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    
    return render(request,'new_post.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.save()
        return redirect('home')
    else:
        form = BusinessForm()
    
    return render(request,'new_business.html',{"form":form})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)

    except DoesNotExist:
        raise Http404()

    business = Business.get_business(project_id)  
    posts = Post.get_post(project_id)

    # is_joined = False
    # if project.join.filter(id = request.user.id).exists():
    #     is_joined = True

    return render(request, 'project.html', {"project": project,"business":business,"posts":posts})

@login_required(login_url='/accounts/login/')
def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)

    except DoesNotExist:
        raise Http404()

    
    return render(request, 'post.html', {"post":post})

# @login_required(login_url='/accounts/login/')
# def new_post(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.poster = current_user
#             post.save()
#         return redirect('home')
#     else:
#         form = PostForm()
    
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        business = Business.search_business(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'business':business})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
        


