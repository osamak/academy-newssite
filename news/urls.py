from django.conf.urls import url

urlpatterns = [
    url(r'^$', "news.views.list_posts", name="list_posts"),
    url(r'^(?P<post_id>\d+)/$', "news.views.show_post", name="show_post"),
    url(r'^(?P<post_id>\d+)/comment/$', "news.views.comment", name="comment"),
]