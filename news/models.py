from django.db import models


class Post(models.Model):
    """
    A news post.
    """
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")

    def has_image(self):
        return self.image != ""

    has_image.boolean = True
    has_image.short_description = "Has Image?"

    def get_summary(self):
        summary = self.body[:200]
        if len(self.body) > 200:
            summary += "..."
        return summary

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """
    A comment on a news post.
    """
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=128)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Comment by %s on post '%s'" % (self.author, self.post.title)
