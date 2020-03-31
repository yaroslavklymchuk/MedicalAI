from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm, Results
from .prediction_processing import make_prediction
from datetime import datetime
from ...tools.logging_config import logger
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from ..subscribe.models import General


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']

            form.created = datetime.now()
            form.save()

            raw_detection_form = DetectionForm()
            result, problem = make_prediction(request)

            logger.info('Result for {}: {}'.format(problem, result))
            result_form = Results.objects.create(email=email, created=datetime.now(), result=result)
            result_form.save()

            logger.info('AUTH: {}'.format(request.user.is_authenticated))

            if request.user.is_authenticated:
                return render(request, "results_detection.html", {'form': raw_detection_form,
                                                                  'result': result,
                                                                  'problem': problem
                                                                  }
                              )
            else:
                return redirect('/subscribe/')
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


