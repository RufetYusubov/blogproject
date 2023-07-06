from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class TagCloudModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class BlogModel(models.Model):
    name = models.CharField(max_length=256)
    pub_date = models.DateField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='posters/',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
    category = models.ManyToManyField(CategoryModel, related_name="category_blogs")
    tag_cloud = models.ManyToManyField(TagCloudModel,related_name="tagcloud_blogs")

    def __str__(self) -> str:
        return self.name
    
class CommentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_comments")
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name="blog_comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE,related_name="replies")
    comment = models.TextField()
    pub_date = models.DateField(auto_now_add = True)


    class Meta:
        verbose_name = "Comment"
        ordering = ("id",)

    def __str__(self):
        return self.user.username + " " + str(self.id)
    
class AboutModel(models.Model):
    name = models.TextField()

    
    def __str__(self) -> str:
        return self.email

    
    