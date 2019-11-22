from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import auth
from django.conf import settings

from profiles.forms import CreateUserForm
from profiles.helpers import submit_client
from profiles.models import *

def login(request):
    # TODO get redir from POST/GET
    redirect_to = request.POST.get('next', request.GET.get('next', settings.LOGIN_REDIRECT_URL))

    if request.user.is_authenticated:
        return redirect(redirect_to)

    if request.method == 'POST':
        req = request.POST
        user = auth.authenticate(username=req['username'], password=req['password'])
        if not user:
            return render(request,'login.html',{'error_message': 'Wrong password'})
        else:
            auth.login(request, user)
            return redirect(redirect_to)

    return render(request,'login.html',{'next': redirect_to})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')


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
