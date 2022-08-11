# ----------------------------------------------------------------------------
# Title:   Configuration parameters
# ----------------------------------------------------------------------------

N_SIGNALS = 17
TEST_SIZE = 0.2
N_LAYERS = {'radar': 3,
            'cems': 3}
N_NEURONS = {'radar': [64, 32, 1],
             'cems': [64, 32, 1]}
ACTIVATION_FUNCTIONS = {'radar': ['tanh', 'tanh', 'relu'],
                        'cems': ['tanh', 'tanh', 'relu']}
N_EPOCHS = {'radar': 40,
            'cems': 20}
VALIDATION_SPLIT = 0.2
LOSS_FUNCTION = 'binary_crossentropy'
OPTIMIZER = 'rmsprop'
