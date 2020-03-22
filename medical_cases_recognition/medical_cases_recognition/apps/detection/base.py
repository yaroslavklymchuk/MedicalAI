from decouple import config


class ModelsConfig:
    MDL_CHEST_X_RAYS = config('MDL_CHEST_X_RAYS')
    WEIGHTS_MDL_CHEST_X_RAYS = config('WEIGHTS_MDL_CHEST_X_RAYS')
    MDL_DIABETIC = config('MDL_DIABETIC')
    WEIGHTS_DIABETIC = config('WEIGHTS_DIABETIC')
    CUTOFF = config('CUTOFF')

