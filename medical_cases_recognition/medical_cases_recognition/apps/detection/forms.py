from django import forms
from .models import DetectionModel, ResultsDetectionModel


class DetectionForm(forms.ModelForm):

    class Meta:
        model = DetectionModel
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(DetectionForm, self).__init__(*args, **kwargs)
        self.fields['img_to_detect'].required = False


class ResultsDetectionForm(forms.ModelForm):

    class Meta:
        model = ResultsDetectionModel
        exclude = [""]
        widgets = {
            'result': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }