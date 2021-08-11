from django.shortcuts import render,get_object_or_404,redirect
from crush.models import CreateUser,PrankList
from django.views.generic import (TemplateView,CreateView,
                                    DetailView,ListView)
from crush.forms import CreateUserForm , PrankListForm

class IndexView(TemplateView):
    template_name = 'crush/index.html'

class CreateUserView(CreateView):

    redirect_field_name = 'crush/detail.html'
    form_class = CreateUserForm
    model = CreateUser


class UserDeatilView(DetailView):
    model = CreateUser

class FooledView(DetailView):
    template_name = 'crush/fooled.html'
    model = CreateUser

# def UserDeatilView(request,num):
#     a = PrankList.objects.all()
#     print(a)
#     return render(request,'detail.html',{})

def pranklistview(request,num):
    a = PrankList.objects.all()
    print(a.yourName)

def calculate(request,num):
    name = get_object_or_404(CreateUser,pk=num)
    if request.method == 'POST':
        form = PrankListForm(request.POST)
        if form.is_valid():
            bakras = form.save(commit=False)
            bakras.prankster = name
            bakras.save()
            return redirect('fooled',pk=num)
    else:
        form = PrankListForm()
    return render(request,'crush/calculate.html',{'form':form})
