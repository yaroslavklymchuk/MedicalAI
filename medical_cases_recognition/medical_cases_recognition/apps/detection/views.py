from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_form = DetectionForm()
            return render(request, "detect.html", {'form': new_form})
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


