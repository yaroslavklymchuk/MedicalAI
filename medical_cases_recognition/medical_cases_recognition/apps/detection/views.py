from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm, ResultsDetectionForm
from .detection import predict, get_model
from .base import ModelsConfig
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from ...settings import MEDIA_ROOT


def preprocess(request, model):
    img_path = request.FILES['img_to_detect'].name
    img = img_to_array(load_img(MEDIA_ROOT + '/images/' + img_path, target_size=(128, 128)))
    img = np.expand_dims(img, axis=0)
    result = predict(model, img, float(ModelsConfig.CUTOFF))

    return result


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            result_form = ResultsDetectionForm()
            model = get_model(ModelsConfig.MDL_CHEST_X_RAYS, ModelsConfig.WEIGHTS_MDL_CHEST_X_RAYS,
                              'medical_cases_recognition/models/', 'medical_cases_recognition/weights/')
            result = preprocess(request, model)
            return render(request, "results_detection.html", {'form': result_form, 'result': result}
                          )
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


