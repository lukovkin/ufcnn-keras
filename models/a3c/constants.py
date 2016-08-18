# -*- coding: utf-8 -*-

### Parameters for A3C
LOCAL_T_MAX = 5 # repeat step size
RMSP_ALPHA = 0.99 # decay parameter for RMSProp
RMSP_EPSILON = 0.1 # epsilon parameter for RMSProp
CHECKPOINT_DIR = 'checkpoints'
LOG_FILE = 'tmp/a3c_log'
INITIAL_ALPHA_LOW = 1e-6    # log_uniform low limit for learning rate (for A3C FF it should be smaller)
INITIAL_ALPHA_HIGH = 1e-4   # log_uniform high limit for learning rate (for A3C FF it should be smaller)

PARALLEL_SIZE = 8# parallel thread size 
ACTION_SIZE = 2 # action size SHORT and LONG

INITIAL_ALPHA_LOG_RATE = 0.4226 # log_uniform interpolate rate for learning rate (around 7 * 10^-4)
GAMMA = 0.99 # discount factor for rewards
ENTROPY_BETA = 0.01 # entropy regularlization constant
MAX_TIME_STEP = 10 * 10**7
GRAD_NORM_CLIP = 40.0 # gradient norm clipping
USE_GPU = False # To use GPU, set True
USE_LSTM = True # True for A3C LSTM, False for A3C FF !!ATTENTION A3C FF is currently not working

### TRADING PARAMETERS
TRAINING_DAYS = 1
TESTING_DAYS = 1
SEQUENCE_LENGTH = 84 * 8 / 4 # = 84 * 84 / 4 - 1
#


# SETUP for TRADCOM input data
FILENAMES = "/prod_data_*v.txt"
STORE_PATH = './training_data_large/' # where to find the training data to load 
FEATURES_LIST = [1,2,3,4] # List of columns from the input that should be used as feature lists
COLGROUPS = [[2,4],[3,5]] # list of lists of columns that should be normalized together
UNMODIFIED_GROUP = [2,4] #  list of columns that should NOT be normalized. Bid and Ask MUST be added here!
BID_COL = 2 # name of the column containing the bid
ASK_COL = 4 # name of the column containing the ask

# SETUP for FDAX-TICKS
FEATURES_LIST=[1,2,'U3',4,5,6,7] 
STORE_PATH ='./training_data_large/' 
FILENAMES = "/FDAX_*.csv"
COLGROUPS = [[1,4,6],[5,7]]
UNMODIFIED_GROUP = [3,4,6] 
BID_COL = 4 
ASK_COL = 6



=======
# Trading fee (per roundturn)
# Stefan: AMP/XTRADER/TTNET: FDAX = 0.125P per roundturn
TRADING_FEE = 0.125

SHOW_TRADES = False # Default, can be overwritten when calling GameState() or Trading()


