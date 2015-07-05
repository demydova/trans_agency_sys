"""trans_agency_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   # url(r'^$', 'homepage.views.home'),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^projects_actual', 'projekt_verwaltung.views.get_projects_actual', name="projects_actual"),
    url(r'^projects/', 'projekt_verwaltung.views.get_projectslist', name='projectslist'),
    url(r'^clients/', 'projekt_verwaltung.views.get_clientslist', name='clientslist'),
    url(r'^translators/', 'projekt_verwaltung.views.get_translatorslist', name='translatorslist'),
    url(r'^ProjectActual/Edit/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.project_details_actual', name="editProjectActual"),
    url(r'^Project/Edit/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.project_details', name="editProject"),
    url(r'^Project/Delete/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.project_delete', name="deleteProject"),
    url(r'^Project/Add/', 'projekt_verwaltung.views.project_details', name="addProject"),
    url(r'^Client/Edit/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.client_details', name="editClient"),
    url(r'^Client/Delete/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.client_delete', name="deleteClient"),
    url(r'^Client/Add/', 'projekt_verwaltung.views.client_details', name="addClient"),
    url(r'^Translator/Edit/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.translator_details', name="editTranslator"),
    url(r'^Translator/Delete/(?P<pk>[0-9]+)?$', 'projekt_verwaltung.views.translator_delete', name="deleteTranslator"),
    url(r'^Translator/Add/', 'projekt_verwaltung.views.translator_details', name="addTranslator"),


   #login
    url(r'^auth/login/$', 'projekt_verwaltung.views.login',),
    url(r'^auth/auth/$', 'projekt_verwaltung.views.auth_view',),
    url(r'^auth/logout/$', 'projekt_verwaltung.views.logout',),
    url(r'^auth/loggedin/$', 'projekt_verwaltung.views.loggedin',),
    url(r'^auth/invalid/$', 'projekt_verwaltung.views.invalid_login',),
]
