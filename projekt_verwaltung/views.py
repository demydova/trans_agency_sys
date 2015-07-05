from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib import auth
from django.core.context_processors import csrf
from projekt_verwaltung.models import *
from projekt_verwaltung.forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
#home

#def home(request):
   # return render(request, "home.html")

def get_projectslist(request):
    projects=Project.objects.all().order_by('start_date')
    return render(request, 'projectslist.html', {'page_title':'List of Projects', 'projects':projects})

def get_clientslist(request):
    clients=Client.objects.all().order_by('login')
    return render(request, 'clientslist.html', {'page_title':'List of Clients', 'clients':clients})

def get_translatorslist(request):
    translators=Translator.objects.all().order_by('login')
    return render(request, 'translatorslist.html', {'page_title':'List of Translators', 'translators':translators})

def get_projects_actual(request):
    projects=Project.objects.filter(end_date__gt=datetime.now).order_by('start_date')
    return render(request, 'projects_actual.html', {'page_title':'List of actual Projects', 'projects':projects})

def client_details(request, pk=None):
    if pk==None:
        client=Client()
        page_title='Add New Client'

    else:
        client=get_object_or_404(Client, pk=pk)
        page_title='Edit Client'
    if request.method=='POST':
        form=ClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
            messages.success(request, u'Client saved successfully')
            return HttpResponseRedirect(reverse('clientslist'))
        else:
            messages.error(request, u'Data incorrect')
        #Fehlermeldung
            pass


    else:
        form=ClientForm(instance=client)

    return render(request, 'client.html', {'page_title': 'Add Client', 'form':form})



def translator_details(request, pk=None):
    if pk==None:
        translator=Translator()
        page_title='Add New Translator'
    else:
        translator=get_object_or_404(Translator, pk=pk)
        page_title='Edit Translator'
    if request.method=='POST':
        form=TranslatorForm(request.POST, instance=translator)
        if form.is_valid:
            form.save()
            messages.success(request, u'Translator saved successfully')
            return HttpResponseRedirect(reverse('translatorslist'))
        else:
            messages.error(request, u'Data incorrect')
        #Fehlermeldung
            pass
    else:
        form=TranslatorForm(instance=translator)
    return render(request, 'translator.html', {'page_title': 'Add Translator', 'form':form})

def project_details(request, pk=None):
    if pk==None:
        project=Project()
        page_title='Add New Project'
    else:
        project=get_object_or_404(Project, pk=pk)
        page_title='Edit Project'
    if request.method=='POST':
        form=ProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            messages.success(request, u'Project saved successfully')
            return HttpResponseRedirect(reverse('projects_actual'))
        else:
            messages.error(request, u'Data incorrect')
        #Fehlermeldung
            pass
    else:
        form=ProjectForm(instance=project)

    return render(request, 'project.html', {'page_title': page_title, 'form':form, })



def project_details_actual(request, pk=None):
    if pk==None:
        project=Project()
        page_title='Add New Project'
    else:
        project=get_object_or_404(Project, pk=pk)
        page_title='Edit Project'
    if request.method=='POST':
        form=ProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            messages.success(request, u'Project saved successfully')
            return HttpResponseRedirect(reverse('projects_actual'))
        else:
            messages.error(request, u'Data incorrect')
        #Fehlermeldung
            pass
    else:
        form=ActualProjectForm(instance=project)
    return render(request, 'actual.html', {'page_title': page_title, 'form':form, })


#delete Funktionen


def project_delete(request, pk=None):
    if Project.objects.get(pk=pk):
        Project.objects.get(pk=pk).delete()
        messages.success(request, u'Project deleted successfully.')
        return HttpResponseRedirect(reverse('projectslist'))
    else:
        messages.error(request, str(pk.description) + u' could not be deleted.')

    pass

def client_delete(request, pk=None):
    if Client.objects.get(pk=pk):
        Client.objects.get(pk=pk).delete()
        messages.success(request, u'Client deleted successfully.')
        return HttpResponseRedirect(reverse('projectslist'))
    else:
        messages.error(request, str(pk.login) + u' could not be deleted.')

    pass

def translator_delete(request, pk=None):
    if Translator.objects.get(pk=pk):
        Translator.objects.get(pk=pk).delete()
        messages.success(request, u'Translator deleted successfully.')
        return HttpResponseRedirect(reverse('projectslist'))
    else:
        messages.error(request, str(pk.login) + u' could not be deleted.')

    pass
#login
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('auth/login.html', c)

def auth_view(request):
    username=request.POST.get('username', '')
    password=request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/auth/loggedin')
    else:
        return HttpResponseRedirect('/auth/invalid')

def loggedin(request):
    return render_to_response('auth/loggedin.html', {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('auth/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('auth/logout.html')




