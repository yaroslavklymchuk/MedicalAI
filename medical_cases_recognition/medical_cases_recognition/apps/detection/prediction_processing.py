from .detection import (predict_x_ray, predict_categorical_problem, get_model, diabet_decisions_mapping,
                        hemorrhage_decisions_mapping)
from .base import ModelsConfig
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from ...settings import MEDIA_ROOT


MODELS_MAPPING = {'Pneumonia': ModelsConfig.MDL_CHEST_X_RAYS,
                  'Diabetic': ModelsConfig.MDL_DIABETIC,
                  'Hemorrhage': ModelsConfig.MDL_HEMORRHAGE
                  }

WEIGHTS_MAPPING = {'Pneumonia': ModelsConfig.WEIGHTS_MDL_CHEST_X_RAYS,
                   'Diabetic': ModelsConfig.WEIGHTS_DIABETIC,
                   'Hemorrhage': ModelsConfig.WEIGHTS_HEMORRHAGE
                   }

CUTOFFS_MAPPING = {'Pneumonia': ModelsConfig.CUTOFF
                   }

TARGET_SIZES_MAPPING = {'Pneumonia': (128, 128),
                        'Diabetic': (128, 128),
                        'Hemorrhage': (224, 224)
                        }

CATEGORIES_MAPPING = {'Diabetic': diabet_decisions_mapping,
                      'Hemorrhage': hemorrhage_decisions_mapping
                      }


def preprocess(request, model, cutoff, problem, target_size, categorical_mapping=None):
    img_path = request.FILES['img_to_detect'].name
    img = img_to_array(load_img(MEDIA_ROOT + '/images/' + img_path, target_size=target_size))
    img = np.expand_dims(img, axis=0)
    if problem == 'Pneumonia':
        result = predict_x_ray(model, img, float(cutoff), problem)
    else:
        result = predict_categorical_problem(model, img, categorical_mapping)

    return result


def define_problem(request):
    problem = request.POST.get('subject')
    mdl = MODELS_MAPPING.get(problem)
    weights = WEIGHTS_MAPPING.get(problem)
    cutoff = CUTOFFS_MAPPING.get(problem)
    target_size = TARGET_SIZES_MAPPING.get(problem)
    categorical_mapping = CATEGORIES_MAPPING.get(problem, None)

    return mdl, weights, cutoff, problem, target_size, categorical_mapping


def make_prediction(request):
    mdl, weights, cutoff, problem, target_size, categorical_mapping = define_problem(request)
    model = get_model(mdl, weights, 'medical_cases_recognition/models/', 'medical_cases_recognition/weights/')
    result = preprocess(request, model, cutoff, problem, target_size, categorical_mapping)

    return result, problem
