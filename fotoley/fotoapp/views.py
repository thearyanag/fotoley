from django.shortcuts import render,redirect
from .models import Profile
from .forms import PostForm

# Create your views here.
# def index(request):
#     return render(request, 'base.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request , 'fotoapp/profile_list.html', {'profiles': profiles})

def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'fotoapp/profile_detail.html', {'profile': profile})

def dashboard(request):
    form = PostForm(request.POST, request.FILES or None)
    print("------------------")
    print(request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    return render(request, 'fotoapp/dashboard.html', {'form': form})