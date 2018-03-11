from django import forms
from . import models

class CreateTodo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ['title','body','slug','thumb']
        

