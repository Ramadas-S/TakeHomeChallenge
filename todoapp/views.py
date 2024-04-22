from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render,redirect
from .models import Project, Todo
from django.contrib import messages

# Create your views here.

def create(request):
    
    return render(request,'createproject.html')


def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            messages.error(request, "Title cannot be empty.")
        elif Project.objects.filter(title=title).exists():
            messages.error(request, "A project with this title already exists.")
        else:
            project = Project.objects.create(title=title)
            return redirect('home', pk=project.pk)
    return render(request, 'createproject.html')


def home(request,pk):
    project = get_object_or_404(Project,pk=pk)
    description=Todo.objects.filter(project=project,completion_status = False).order_by('-updated_date')
    completed_task=Todo.objects.filter(project=project,completion_status = True)
    
    context ={
        'descriptions':description,
        'completed_tasks':completed_task,
        'project':project
    }

    return render(request,'home.html',context)


def addTask(request, project_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description:
            project = get_object_or_404(Project, pk=project_id)
            Todo.objects.create(description=description, project=project)
            return redirect('home', pk=project_id)  # Redirect back to the home page for the specific project
    return render(request, 'add_task.html') 


def mark_as_done(request,desc_id):
    description = get_object_or_404(Todo,pk=desc_id)
    description.completion_status = True
    description.save()

    return redirect('home', pk=description.project.pk)


def mark_as_undone(request,desc_id):
    todo = get_object_or_404(Todo, pk=desc_id)
    todo.completion_status = False
    todo.save()

    return redirect('home',pk=todo.project.pk)

def delete_task(request,desc_id):
    description = get_object_or_404(Todo,pk=desc_id)
    description.delete()
    return redirect('home',pk=description.project.pk)

def edit_task(request,desc_id):
    description = get_object_or_404(Todo,pk=desc_id)
    if request.method == 'POST':
        new_description = request.POST.get('description')
        description.description = new_description
        description.save()
        return redirect('home',pk=description.project.pk)
    else:
        context = {
            'description':description,
        }
        return render(request,'edit.html',context)
    

def project_detail(request,prj_id):
    project = get_object_or_404(Project,pk=prj_id)
    description = Todo.objects.filter(project=project, completion_status=False).order_by('-updated_date')
    completed_task = Todo.objects.filter(project=project, completion_status=True)
    
    context ={
        'project':project,
        'description':description,
        'completed_task':completed_task,
    }
    
    
    return render(request,'projectdetail.html',context)


def edit_project(request,prj_id):
    project = get_object_or_404(Project,pk=prj_id)
    if request.method == 'POST':
        new_project_name = request.POST.get('title')
        if new_project_name != project.title:
            if Project.objects.filter(title=new_project_name).exists():
                context ={
                    'project':project,
                    'error_message': 'Project with this title already exists.'
                }
                return render(request, 'projectdetail.html', context)
        project.title = new_project_name
        project.save()
        return redirect('home',pk=project.pk)
    else:
        context = {
            'project':project,
        }
        return render(request,'projectdetail.html',context)