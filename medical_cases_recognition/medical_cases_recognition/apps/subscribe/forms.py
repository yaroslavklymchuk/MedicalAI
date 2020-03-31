from django import forms
from .models import General, User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['last_login'].required = False
        self.fields['last_login'].widget = forms.HiddenInput()
        self.fields['user_permissions'].required = False
        self.fields['user_permissions'].widget = forms.HiddenInput()
        self.fields['groups'].required = False
        self.fields['groups'].widget = forms.HiddenInput()
        self.fields['is_staff'].required = False
        self.fields['is_staff'].widget = forms.HiddenInput()
        self.fields['is_superuser'].required = False
        self.fields['is_superuser'].widget = forms.HiddenInput()
        self.fields['is_active'].required = False
        self.fields['is_active'].widget = forms.HiddenInput()


class GeneralForm(forms.ModelForm):

    class Meta:
        model = General
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(GeneralForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['user'].widget = forms.HiddenInput()


