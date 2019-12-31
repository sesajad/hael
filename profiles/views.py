from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from profiles.forms import CreateUserForm
from profiles.helpers import submit_client
from profiles.models import *


@login_required
def register(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            context = {
                'form': CreateUserForm(),
                }
            return render(request, 'register.html', context)
        else:
            return HttpResponseForbidden('Must be superuser')
    elif request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.set_password(form.cleaned_data['password'])
            inst.save()
            return redirect('index')
        else:
            context = {
                'form': form,
                }
            return render(request, 'register.html', context)


@login_required
def index(request):
    client_ip, expire_time = submit_client(request)
    return render(request, 'index.html', {'client_ip': client_ip, 'expire_time': expire_time, 'registered_ips':
        request.user.ipspec_set.all()})
