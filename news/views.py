from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from news.models import Post, Comment


def list_posts(request):
    posts = Post.objects.all().order_by("-pub_date")[:10]
    comments = Comment.objects.all().order_by("-pub_date")[:5]
    context = {"posts": posts, "comments": comments}
    return render(request, "news/list_posts.html", context)


def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, "news/show_post.html", context)


def comment(request, post_id):
    if not request.method == "POST":
        raise Http404

    # FIXME: Empty `author` and `body` fields shouldn't be accepted
    new_comment = Comment(post=Post.objects.get(id=post_id),
                          author=request.POST.get("author"),
                          body=request.POST.get("body"))
    new_comment.save()
    return HttpResponseRedirect(reverse("news:show_post", args=(post_id, )))

# FIXME: Spice up the application a bit.
