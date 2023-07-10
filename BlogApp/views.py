from django.shortcuts import render,redirect
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel,CommentModel,AboutModel
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        blogs = BlogModel.objects.order_by("-id")[:3]
        categories = CategoryModel.objects.all()
        tagclouds = TagCloudModel.objects.all()

        context = {
            'blogs' : blogs,
            'categories' : categories,
            'tagclouds' : tagclouds
        }

        return render(request,"index.html",context)
#-----------------------------------------------------------------------------------------

class CategoryView(View):
    def get(self,request,id,*args,**kwargs):
        category = CategoryModel.objects.get(id=id)
        categories = CategoryModel.objects.all()
        blogs = BlogModel.objects.filter(category=category)

        context = {
            'category' : category,
            'categories' : categories,
            'blogs' : blogs
        }

        return render(request,"categories.html",context)
#-------------------------------------------------------------------------------------------------
class TagCloudView(View):
    def get(self,request,id,*args,**kwargs):
        tagcloud = TagCloudModel.objects.get(id=id),
        tagclouds = TagCloudModel.objects.all()
        blogs = BlogModel.objects.filter(tag_cloud=tagcloud)

        context = {
            'tagcloud' : tagcloud,
            'tagclouds' : tagclouds,
            'blogs' : blogs
        }

        return render(request,'tagcloud.html',context)
#--------------------------------------------------------------------------------------------------
class PostDetailView(View):
    def get(self,request,id,*args,**kwargs):
        categories = CategoryModel.objects.all()
        tagclouds = TagCloudModel.objects.all()

        blog = BlogModel.objects.get(id=id)
        blogs = BlogModel.objects.order_by("-id")
        blog_comments = CommentModel.objects.filter(
            blog = blog,
            parent = None
        )
        context = {
            "blog" : blog,
            "blogs" : blogs,
            "categories" : categories,
            "tagclouds" : tagclouds,
            "blog_comments" : blog_comments
        }
        if request.user.is_authenticated:
            user_comments = CommentModel.objects.filter(
                user = request.user
            )
            context["user_comments"] = user_comments

        return render(request,'post-details.html',context)
    
    def post(self,request,id,*args,**kwargs):
        choice = request.POST.get("choice")
        if choice == "comment":
            comment = request.POST.get("comment")
            blog_id = request.POST.get("blog_id")

            blog = BlogModel.objects.get(id=blog_id)

            CommentModel.objects.create(
                user = request.user,
                blog = blog,
                comment = comment,
                
            )

        elif choice == "reply":
            reply = request.POST.get("reply")

            blog_id = request.POST.get("blog_id")
            blog = BlogModel.objects.get(id=blog_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            CommentModel.objects.create(
                user = request.user,
                blog = blog,
                comment = reply,
                parent = comment
            )

            return redirect("post-details",id=id)
        
#------------------------------------------------------------------------------------
class AboutView(View):
    def get(self,request,*args,**kwargs):
        about = AboutModel.objects.first()
        context = {
            'about' : about
        }

        return render(request,'about.html',context)
    
#--------------------------------------------------------------------------------------



