import logging

from django import forms
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate
from django import forms
from django_summernote.widgets import SummernoteWidget


from .form_utils import BootstrapForm, RegexPasswordValidator
from website import models



class OperatorLoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label_suffix="*",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message='Enter a valid email.'
            )
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label_suffix="*"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is not None:
                try:
                    operator = models.Operator.objects.get(user=user, is_active=True)
                except models.Operator.DoesNotExist:
                    logging.warning("OperatorLoginForm; clean; Operator does not exist or is not active")
                    raise forms.ValidationError("Invalid user credentials")
            else:
                logging.warning("OperatorLoginForm; clean; User does not exist")
                raise forms.ValidationError("Invalid user credentials")

        return cleaned_data


class AdminPageForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = models.Page
        fields = "__all__"
        widgets = {
            "content": SummernoteWidget(
                attrs={"class": "django_ckeditor_5"}
            )
        }