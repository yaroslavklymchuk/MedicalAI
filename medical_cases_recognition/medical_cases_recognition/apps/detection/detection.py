from tensorflow.keras.models import model_from_json
from ...tools.logging_config import logger


diabet_decisions_mapping = {0: 'Mild',
                            1: 'Severe',
                            2: 'Proliferate DR',
                            3: 'No DR',
                            4: 'Moderate'
                            }

hemorrhage_decisions_mapping = {0: 'Epidural Hemorrhage',
                                1: 'Intraparenchymal Hemorrhage',
                                2: 'Intraventricular Hemorrhage',
                                3: 'Subarachnoid Hemorrhage',
                                4: 'Subdural Hemorrhage',
                                5: 'No Hemorrhage'
                                }


def get_model(mdl, weights, path_mdl, path_weights):
    json_file = open(path_mdl+mdl, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(path_weights+weights)
    loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return loaded_model


def predict_x_ray(mdl, img, cutoff, decision):
    prediction = mdl.predict(img)[0][0]

    logger.info('Predicted probability: {}'.format(prediction))

    if prediction >= cutoff:
        return decision
    else:
        return 'No {}'.format(decision)


def predict_categorical_problem(mdl, img, decisions_mapping):
    prediction = mdl.predict(img).argmax()
    mapped_prediction = decisions_mapping.get(prediction)

    logger.info('Predicted probability: {}'.format(mdl.predict(img).max()))

    return mapped_prediction

