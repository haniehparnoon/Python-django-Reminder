from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Q,Count
import datetime
from .models import *


class TaskList(ListView):
    model = Task
    def get(self, request):
        sort_by = request.GET.get("sort", "l") 
        if sort_by == "l":
            tasks = Task.objects.all()
        else:
             tasks = Task.objects.all().order_by("due_date") 
        return render(request,'todo/task_list.html', {'tasks':tasks})

    def post(self, req):
        if req.method == 'POST'  and req.is_ajax():
            text = req.POST.get('text')
            print("TEXT",text)
            now = datetime.datetime.now()
            expired_task = Task.objects.filter(Q(due_date__lt=now) | Q(due_date=None))
            unexpired_task = Task.objects.filter(Q(due_date__gt=now) | Q(due_date=None))
            last_task = Task.objects.all().order_by("-due_date")[:3]
            if text == "ExpiredTasks":
                p_all = expired_task
                print(p_all)
            elif text == "UnexpiredTasks" :  
                p_all =  unexpired_task
            elif text == "LastTasks":
                p_all =  last_task

                    
            if p_all:
                return JsonResponse({
                    'tasks':list(p_all.values_list('title', flat=True))
                })
            else:
                return JsonResponse({
                    'tasks': [],
                    'msg' : "doesn't match any files",
                })

           
            
        else:
            return render(request,'todo/task_list.html')  

    
class TaskDetail(DetailView):
    model = Task


class CategoryList(ListView):
    model = Category
    def post(self, req):
        empty_categories=[]
        if req.method == 'POST'  and req.is_ajax():
            text = req.POST.get('text')
            popular = Category.objects.annotate(Count('task')).order_by('-task__count')[:3]
            popular_categories = list(popular.values_list('category_name', flat=True))
  
            print("POPULAR:",popular_categories)
            print("TYPE",type(popular_categories))
            #find empty task
            allCat = Category.objects.all()
            for Cat in allCat:
                empty= Cat.task_set.all().values()
                if  not(empty.exists()):
                    empty_categories.append(Cat.category_name)
                   

                    print("POPULAR:",popular_categories)
                    print("TYPE",type(Cat))


            # popular_categories= Task-set.all()
               
            if text == "EmptyCategories":
                p_all = empty_categories
                
            elif text == "PopularCategories" :  
                p_all =  popular_categories
                    
            if p_all:
                return JsonResponse({
                    'category':p_all
                })
            else:
                return JsonResponse({
                    'category': [],
                    'msg' : "doesn't match any files",
                })

           
            
        else:
            return render(request,'todo/task_list.html')  

    
       
class CategoryDetail(DetailView):
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoryTasks"] = Task.objects.all().filter(category = context["category"])
        return context
    


def add_task(req):
    if req.method == 'POST' and req.is_ajax():
        category = req.POST.get('categoryy')
        title = req.POST.get('titlee')
        description = req.POST.get('descriptionn')
        priority = req.POST.get('priorityy')
        due_date = req.POST.get('due_datee')
        find_category = Category.objects.all().filter(category_name = category)
        task = Task.objects.create( title=title, description=description,Priority=priority,due_date=due_date)
        if find_category.exists():
            # task.category.add(find_category)
            ids = find_category.values_list('pk', flat=True)
            id_list = list(ids)
            #print("TYPE:",id_list[0])
            task.category.add(id_list[0])
            
        else:   
            category = Category.objects.create(category_name = category)
            task.category.add(category)

        return JsonResponse({})  

    else:
        return render(req, "todo/add_task.html")


def home(req):
    last_tasks = Task.objects.all().order_by("-due_date")[:3]
    print(last_tasks)

    return render(req,"todo/home.html",{"last_tasks":last_tasks})   


def add_category(req):
    if req.method == 'POST' and req.is_ajax():
        category = req.POST.get('category')
        description = req.POST.get('description')
        category = Category.objects.create(category_name = category,  description =  description)
            
        return JsonResponse({})  

    else:
        return render(req, "todo/add_category.html")
    

