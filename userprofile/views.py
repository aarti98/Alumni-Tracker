from django.shortcuts import render
from post.models import Post

def display_post(request):
    logged_in_user = request.user
    logged_in_user_post = Post.objects.filter(user=logged_in_user)
    context = {'posts': logged_in_user_post}

    return render(request, 'userprofile/post_list.html', context)
