from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from employee.forms import UserForm 




def employee_list(request):
    context ={}
    context['users'] =  User.objects.all()
    context['title'] = 'Employee'
    return render(request, 'employee/index.html', context)

def employee_detail(request):

    context ={}
    context['user'] = get_object_or_404(User, id=id)
    return render(request,'employee/index.html', context)

def employee_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', {"user_form":user_form})

    else:
        user_form = UserForm()
        return render(request, 'employee/add.html', {"user_form":user_form})


