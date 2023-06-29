from django.shortcuts import render
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        blogs = BlogModel.objects.order_by("-id")[:3]
        categories = CategoryModel.objects.all()

        context = {
            'blogs' : blogs,
            'categories' : categories
        }

        return render(request,"home.html",context)

class CategoryView(View):
    def get(self,request,id,*args,**kwargs):
        category = CategoryModel.objects.get(id=id)
        categories = CategoryModel.objects.all()

        context = {
            'category' : category,
            'categories' : categories
        }

        return render(request,"categories.html",context)



