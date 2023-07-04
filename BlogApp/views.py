from django.shortcuts import render,redirect
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel,CommentModel
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

        context = {
            'category' : category,
            'categories' : categories
        }

        return render(request,"categories.html",context)
#--------------------------------------------------------------------------------------------------
class PostDetailView(View):
    def get(self,request,id,*args,**kwargs):
        categories = CategoryModel.objects.all()
        tagclouds = TagCloudModel.objects.all()

        blog = BlogModel.objects.get(id=id)
        blogs = BlogModel.objects.order_by("-id")
        context = {
            "blog" : blog,
            "blogs" : blogs,
            "categories" : categories,
            "tagclouds" : tagclouds
        }

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



