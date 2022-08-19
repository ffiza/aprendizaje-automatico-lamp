# ----------------------------------------------------------------------------
# Title:   Configuration parameters
# ----------------------------------------------------------------------------

N_SIGNALS = 17
TEST_SIZE = 0.2
VALIDATION_SPLIT = 0.2
LOSS_FUNCTION = 'binary_crossentropy'
OPTIMIZER = 'rmsprop'

# Definition of the parameters of each model
models_params = {'m0': {'N_LAYERS':             3,
                        'N_NEURONS':            [64, 32, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'relu'],
                        'N_EPOCHS':             20,
                        'COLOR':                'tab:blue'},
                 'm1': {'N_LAYERS':             3,
                        'N_NEURONS':            [64, 32, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'relu'],
                        'N_EPOCHS':             40,
                        'COLOR':                'tab:orange'},
                 'm2': {'N_LAYERS':             4,
                        'N_NEURONS':            [64, 32, 16, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'tanh',
                                                 'relu'],
                        'N_EPOCHS':             40,
                        'COLOR':                'tab:green'},
                 'm3': {'N_LAYERS':             4,
                        'N_NEURONS':            [64, 32, 16, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'relu',
                                                 'relu'],
                        'N_EPOCHS':             40,
                        'COLOR':                'tab:red'},
                 'm4': {'N_LAYERS':             5,
                        'N_NEURONS':            [64, 32, 16, 8, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'relu',
                                                 'relu', 'relu'],
                        'N_EPOCHS':             40,
                        'COLOR':                'tab:purple'},
                 'm5': {'N_LAYERS':             5,
                        'N_NEURONS':            [64, 32, 16, 8, 1],
                        'ACTIVATION_FUNCTIONS': ['tanh', 'tanh', 'relu',
                                                 'relu', 'relu'],
                        'N_EPOCHS':             60,
                        'COLOR':                'tab:brown'},
                 }
