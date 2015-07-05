__author__ = 'annademydova'
from django.forms import *
from projekt_verwaltung.models import *

#class AuthorForm(Form):
 #   fn=CharField(required=True, lable='First Name')

class ClientForm(ModelForm):
    class Meta:
        model=Client
        labels={
            'ln':'Last Name',
            'fn':'First Name',
        }
        fields = "__all__"

class TranslatorForm(ModelForm):
    class Meta:
        model=Translator
        labels={
            'ln':'Last Name',
            'fn':'First Name',
        }
        fields = "__all__"


class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields = "__all__"

class ActualProjectForm(ModelForm):
    class Meta:
        model=Project
        fields = "__all__"

