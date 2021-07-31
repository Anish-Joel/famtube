from django.shortcuts import redirect, render,get_object_or_404
from .forms import VodForm
from .models import Vod
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (CreateView,UpdateView,ListView,DetailView,DeleteView)
# Create your views here.
def vodlist(request):
    queryset=  Vod.objects.all()
    context ={
        "object_list":queryset
    }
    return render(request,'maa.html',context)
def detail(request,id):
    obj = get_object_or_404(Vod,id = id)
    context ={
        "object":obj
    }
    return render(request,'ma.html',context)
    
def vodcreate(request):
    form = VodForm(request.POST or  None)
    if form.is_valid():
        form.save()
        form =VodForm()
        return redirect('../../')
    context ={
        "form":form
    }
    return render(request,'taa.html',context)
def voddelete(request,id):
    obj = get_object_or_404(Vod,id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context ={
        "object":obj
    }
    return render(request,'t.html',context)
    
def vodupdate(request,id):
    obj = get_object_or_404(Vod,id = id)
 
    form = VodForm(request.POST or  None,instance =obj)
    if form.is_valid():
        form.save()
        form =VodForm()
        return redirect('../../')
    context ={
        "form":form
    }
    return render(request,'taa.html',context)
    