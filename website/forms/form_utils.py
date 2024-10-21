import re
from django.utils.translation import gettext as _
from django import forms


class RegexPasswordValidator:
    def __init__(self, pattern, message=None):
        self.pattern = pattern
        self.message = message or _("Password does not match the required pattern.")

    def validate(self, password, user=None):
        if not re.match(self.pattern, password):
            raise forms.ValidationError(self.message, code='password_no_match')

    def get_help_text(self):
        return self.message


class BootstrapForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_class()

    def add_form_class(self):
        for field_name, field in self.fields.items():
            if type(field) == forms.BooleanField:
                continue
            if type(field) == forms.DateField:
                field.widget = forms.DateInput(attrs={"type": "date"})

            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control border-1 py-3 my-1 mb-4'.strip()
