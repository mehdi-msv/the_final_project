from django.forms import ModelForm
from blog.models import *



class CommentForm(ModelForm):
    
    class Meta:
        
        model = Comment

        fields = ['post','email','name','subject','content']


