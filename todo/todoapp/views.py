
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import todoform
from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView


class classviews(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


class classdetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class classupdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['task','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class classdelete(DeleteView):
    model = Task
    template_name = 'del.html'
    success_url = reverse_lazy('cbvhome')
# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        task1 = request.POST.get('task1','')
        prior = request.POST.get('prior1','')
        date1 = request.POST.get('date1','')
        task = Task(task=task1, priority=prior, date=date1)
        task.save()
    return render(request, 'home.html', {'task': task1})


# def detail(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task1})


def delete(request,taskid,):
    if request.method=="POST":
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'del.html')

def update(request,id):
    task = Task.objects.get(id=id)
    form1 = todoform(request.POST or None, instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form1})



