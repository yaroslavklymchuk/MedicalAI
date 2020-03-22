from tensorflow.keras.models import model_from_json
from ...tools.logging_config import logger


diabet_decisions_mapping = {0: 'Mild',
                            1: 'Severe',
                            2: 'Proliferate_DR',
                            3: 'No_DR',
                            4: 'Moderate'
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


def predict_diabet(mdl, img):
    prediction = mdl.predict(img).argmax()
    mapped_prediction = diabet_decisions_mapping.get(prediction)

    logger.info('Predicted probability: {}'.format(mdl.predict(img).max()))

    return mapped_prediction

