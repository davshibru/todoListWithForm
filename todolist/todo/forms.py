from django import forms

from .models import TodoMod

class TodoForm(forms.ModelForm):

	class Meta:
		model = TodoMod
		fields = ('action','status',)
			
	
