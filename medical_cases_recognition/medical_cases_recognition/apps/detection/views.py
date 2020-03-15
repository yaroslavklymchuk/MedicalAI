from django.http import HttpResponse
from django.shortcuts import render
from .forms import DetectionForm
from .detection import predict, get_model
from .base import ModelsConfig
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from ...settings import MEDIA_ROOT


def ResponseForDetection(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_form = DetectionForm()
            model = get_model(ModelsConfig.MDL_CHEST_X_RAYS, ModelsConfig.WEIGHTS_MDL_CHEST_X_RAYS,
                              'medical_cases_recognition/models/', 'medical_cases_recognition/weights/')

            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            img_path = request.FILES['img_to_detect'].name
            img = img_to_array(load_img(MEDIA_ROOT + '/images/' + img_path, target_size=(128, 128)))
            img = np.expand_dims(img, axis=0)
            result = predict(model, img, float(ModelsConfig.CUTOFF))
            return render(request, "detect.html", {'form': new_form,
                                                   'result': result}
                          )
        else:
            return HttpResponse('image upload failed with errors: {}'.format(form.errors))
    else:
        form = DetectionForm()
    return render(request, "detect.html", {'form': form})


