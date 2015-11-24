from django import forms
from tinymce.widgets import TinyMCE

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class AddProjectForm(forms.Form):
    title = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title here...'}))
    shortname = forms.CharField(max_length=32,  
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter shortname/alias for project...'}))
    description = forms.CharField(widget=TinyMCE(attrs={'width':'100%', 'cols': 80, 'rows': 80}, mce_attrs={'width': '100%'}))

class AddTaskForm(forms.Form):
	TASK_TYPES = (('Feature', 'Feature'), 
			('Bug', 'Bug'), 
			('Enhancement', 'Enhancement'))
	
	TASK_PRIORITY = (('Low', 'Low'), 
			('Medium', 'Medium'), 
			('High', 'High'))

	title = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title here...'}))
        description = forms.CharField(widget=TinyMCE(attrs={'width':'100%', 'cols': 80, 'rows': 80}, mce_attrs={'width': '100%'}))
	type = forms.ChoiceField(choices=TASK_TYPES, required=True, label='Type')
	priority = forms.ChoiceField(choices=TASK_PRIORITY, required=True, label='Priority')

class AddTodoForm(forms.Form):
    note = forms.CharField(max_length=128, 
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note...'}))

class AddCommentForm(forms.Form):
	title = forms.CharField(max_length=128, 
			widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter comment title here...'}))
        description = forms.CharField(widget=TinyMCE(attrs={'width':'100%', 'cols': 80, 'rows': 80}, mce_attrs={'width': '100%'}))
