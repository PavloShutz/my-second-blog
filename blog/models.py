from django.db import models

# Text, title, author, likes, dislikes
# Published date, created date, edited date
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField(help_text="Here comes your magic...")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    cr_date = models.DateTimeField("date created")
    pub_date = models.DateTimeField("date published", blank=True, null=True)
    edit_date = models.DateTimeField("date edited", blank=True, null=True)
    title_image = models.ImageField(upload_to="post_title_images", default='placeholder.png')

    def __str__(self):
        return self.post_title


# Text, author, likes, dislikes
# Published date, edited date
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(help_text="Here comes your magic...")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")
    edit_date = models.DateTimeField("date edited")
