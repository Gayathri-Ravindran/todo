from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import Task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name = 'new1'

class taskdetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class taskupdateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdeatil',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    new = Task.objects.all()
    if request.method =='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'new1':new})

def delete_view(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'form':f,'task':task})


