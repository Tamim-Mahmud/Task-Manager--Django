from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from tempus_dominus.widgets import DateTimePicker



class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='',widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Email'}))
    first_name=forms.CharField(label='',max_length="50",widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label='',max_length="50",widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must contain at least 8 characters.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
from django import forms
from .models import Tasks_list

PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

class AddTaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', 'label': ''}),
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control', 'label': ''}),
        required=False,
    )
    
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'label': False}),
    )
    
    due_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'placeholder': 'Due Date','type':'datetime-local', 'class': 'form-control', 'label': ''}),
    )
    
    priority = forms.IntegerField(
        widget=forms.Select(choices=PRIORITY_CHOICES, attrs={'class': 'form-control', 'label': ''}),
        initial=2,  # Default to Medium
    )
    
    is_complete = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'label': ''}),
    )
    
    class Meta:
        model = Tasks_list
        exclude = ('user', 'creation_date', 'last_update_date')
        

        
    
