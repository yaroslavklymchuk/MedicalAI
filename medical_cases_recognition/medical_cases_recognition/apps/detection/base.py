from decouple import config


class ModelsConfig:
    MDL_CHEST_X_RAYS = config('MDL_CHEST_X_RAYS')
    WEIGHTS_MDL_CHEST_X_RAYS = config('WEIGHTS_MDL_CHEST_X_RAYS')
    CUTOFF = config('CUTOFF')

