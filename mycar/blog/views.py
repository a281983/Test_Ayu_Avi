from django.shortcuts import render, get_object_or_404


# Create your views here.


from .models import Post

def post_list(request):
   posts = Post.published.all()
   return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, year, month, day, post):
   post = get_object_or_404(Post, slug=post,
                                  status='published',
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
   return render(request,
                 'blog/post/detail.html',
                 {'post': post})



#Adding a line to check git
#Adding another line to check git
#Adding 3rd line to check git
#Adding 4thline to check git
#Ayu adding the 5th line.
