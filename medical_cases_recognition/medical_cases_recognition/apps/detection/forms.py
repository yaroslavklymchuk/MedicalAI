from django import forms
from .models import DetectionModel


class DetectionForm(forms.ModelForm):

    class Meta:
        model = DetectionModel
        exclude = [""]

    def __init__(self, *args, **kwargs):
        super(DetectionForm, self).__init__(*args, **kwargs)
        self.fields['img_to_detect'].required = False
