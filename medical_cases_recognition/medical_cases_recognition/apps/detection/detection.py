from tensorflow.keras.models import model_from_json


def get_model(mdl, weights, path_mdl, path_weights):
    json_file = open(path_mdl+mdl, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(path_weights+weights)

    return loaded_model


def predict(mdl, img, cutoff):
    prediction = mdl.predict(img)[0][0]

    if prediction >= cutoff:
        return 'Pneumonia'
    else:
        return 'No Pneumonia'

