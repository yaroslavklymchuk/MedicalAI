from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm
from .prediction_processing import make_prediction


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            result_form = DetectionForm()
            result = make_prediction(request)

            return render(request, "results_detection.html", {'form': result_form, 'result': result}
                          )
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


