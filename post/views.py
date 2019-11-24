from django.shortcuts import render,redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddPost

@login_required
def add_post(request):
    if request.method=='POST':
        form = AddPost(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect(reverse('homepage'))
    
    else:
        form = AddPost()

    return render(request, 'post/addpost.html', {'form':form})