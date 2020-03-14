from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "detect.html", {'form': form})
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


