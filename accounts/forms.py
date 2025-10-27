from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, AvailableClass
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True)  # Ensure username is included
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    bio = forms.CharField(max_length=255)
    major = forms.CharField(max_length=255)
    classes = forms.ModelMultipleChoiceField(
        queryset=AvailableClass.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'bio', 'major', 'classes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('bio', css_class='form-control'),
            Field('major', css_class='form-control'),
            Field('classes', css_class='form-check')
        )


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    major = forms.CharField(max_length=255)
    classes = forms.ModelMultipleChoiceField(queryset=AvailableClass.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'bio', 'major', 'classes')

