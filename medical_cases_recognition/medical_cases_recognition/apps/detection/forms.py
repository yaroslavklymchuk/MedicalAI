from django import forms
from .models import Detection, Results


class DetectionForm(forms.ModelForm):

    class Meta:
        model = Detection
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(DetectionForm, self).__init__(*args, **kwargs)
        self.fields['img_to_detect'].required = False
        self.fields['created'].widget = forms.HiddenInput()
        self.fields['created'].required = False


class ResultsForm(forms.ModelForm):

    class Meta:
        model = Results
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(ResultsForm, self).__init__(*args, **kwargs)
        self.fields['created'].widget = forms.HiddenInput()
        self.fields['created'].required = False
        self.fields['result'].required = False
        self.fields['email'].required = False


