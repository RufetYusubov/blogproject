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
            'tagclouds' : tagclouds,
        }


        return render(request,"index.html",context)

#--------------------------------------------------------------------

def search_view(request):
    search = request.GET.get('search') 
    results = BlogModel.objects.filter(name__contains=search) 
    categories = CategoryModel.objects.all()
    tagclouds = TagCloudModel.objects.all()
    blogs = BlogModel.objects.all()

    context = {
        'results': results,
        'categories' : categories,
        'tagclouds' : tagclouds,
        'blogs' : blogs,
    }
    
    return render(request, 'search_results.html', context)

#-----------------------------------------------------------------------------------------

class CategoryView(View):
    def get(self,request,id,*args,**kwargs):
        category = CategoryModel.objects.get(id=id)
        categories = CategoryModel.objects.all()

        blogs = BlogModel.objects.all()
        category_blogs = BlogModel.objects.filter(category=category)
        tagclouds = TagCloudModel.objects.all()

        context = {
            'category' : category,
            'categories' : categories,
            'blogs' : blogs,
            'category_blogs' :  category_blogs,
            'tagclouds' : tagclouds
        }

        return render(request,"categories.html",context)
#-------------------------------------------------------------------------------------------------
class TagCloudView(View):
    def get(self,request,id,*args,**kwargs):
        tagcloud = TagCloudModel.objects.get(id=id)
        tagclouds = TagCloudModel.objects.all()

        categories = CategoryModel.objects.all()
        blog_tags= BlogModel.objects.filter(tag_cloud=tagcloud)
        blogs = BlogModel.objects.all()

        context = {
            'tagcloud' : tagcloud,
            'tagclouds' : tagclouds,
            'categories' : categories,
            'blog_tags' :blog_tags,
            'blogs' : blogs
        }

        return render(request,'tagcloud.html',context)
#----------------------------------------------------------------------------------------------
class BlogView(View):
    def get(self,request,*args,**kwargs):
        blogs = BlogModel.objects.all()
        tagclouds = TagCloudModel.objects.all()
        categories = CategoryModel.objects.all()

        context = {
            'blogs' : blogs,
            'tagclouds' : tagclouds,
            'categories' : categories
        }

        return render(request,'blog.html',context)
#---------------------------------------------------------------------------------------------
class PostDetailView(View):
    def get(self,request,id,*args,**kwargs):
        categories = CategoryModel.objects.all()
        tagclouds = TagCloudModel.objects.all()
        blogs = BlogModel.objects.all()
        blog = BlogModel.objects.get(id=id)

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
            if request.user.is_authenticated:
                name = request.user.first_name
                surname = request.user.last_name
            else:
                name = request.POST.get("name")
                surname = request.POST.get("surname")
                email = request.POST.get("email")
            comment = request.POST.get("comment")
            
            blog_id = request.POST.get("blog_id")
            blog = BlogModel.objects.get(id=blog_id)

            if request.user.is_authenticated:
                CommentModel.objects.create(
                    user = request.user,
                    blog = blog,
                    comment = comment,
                    name = name,
                    surname = surname,             
                )
            else:
                 CommentModel.objects.create(
                    blog = blog,
                    comment = comment,
                    name = name,
                    surname = surname,
                    email = email    
                )



        elif choice == "reply":
            reply = request.POST.get("reply")
            if request.user.is_authenticated:
                    name = request.user.first_name
                    surname = request.user.last_name
            else:
                name = request.POST.get("name")
                surname = request.POST.get("surname")
                email = request.POST.get("email")
            comment = request.POST.get("comment")

            blog_id = request.POST.get("blog_id")
            blog = BlogModel.objects.get(id=blog_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            if request.user.is_authenticated:
                CommentModel.objects.create(
                    user = request.user,
                    blog = blog,
                    comment = reply,
                    parent = comment,
                    name = name,
                    surname = surname,
                    email = email
                )
            else:
                 CommentModel.objects.create(
                    blog = blog,
                    comment = reply,
                    parent = comment,
                    name = name,
                    surname = surname,
                    email = email
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
def DeleteComment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect("post-details", id=comment.blog.id)
