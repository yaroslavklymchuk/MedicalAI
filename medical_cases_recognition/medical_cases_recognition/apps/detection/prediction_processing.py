from .detection import predict_x_ray, predict_diabet, get_model
from .base import ModelsConfig
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from ...settings import MEDIA_ROOT


MODELS_MAPPING = {'Pneumonia': ModelsConfig.MDL_CHEST_X_RAYS,
                  'Diabetic': ModelsConfig.MDL_DIABETIC
                  }

WEIGHTS_MAPPING = {'Pneumonia': ModelsConfig.WEIGHTS_MDL_CHEST_X_RAYS,
                   'Diabetic': ModelsConfig.WEIGHTS_DIABETIC
                   }

CUTOFFS_MAPPING = {'Pneumonia': ModelsConfig.CUTOFF
                   }


def preprocess(request, model, cutoff, problem):
    img_path = request.FILES['img_to_detect'].name
    img = img_to_array(load_img(MEDIA_ROOT + '/images/' + img_path, target_size=(128, 128)))
    img = np.expand_dims(img, axis=0)
    if problem == 'Pneumonia':
        result = predict_x_ray(model, img, float(cutoff), problem)
    else:
        result = predict_diabet(model, img)

    return result


def define_problem(request):
    problem = request.POST.get('subject')
    mdl = MODELS_MAPPING.get(problem)
    weights = WEIGHTS_MAPPING.get(problem)
    cutoff = CUTOFFS_MAPPING.get(problem)

    return mdl, weights, cutoff, problem


def make_prediction(request):
    mdl, weights, cutoff, problem = define_problem(request)
    model = get_model(mdl, weights, 'medical_cases_recognition/models/', 'medical_cases_recognition/weights/')
    result = preprocess(request, model, cutoff, problem)

    return result, problem
