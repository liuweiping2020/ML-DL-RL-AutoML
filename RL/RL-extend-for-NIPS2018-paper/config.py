'''
    environment related
'''
NUM_POLICIES = 1
ACTION_DIM = 1
ACTION_SPACE = 5
OBSERVATION_SPACE = 3
STOP_REWARD = 30
R_EXPAND = 0.1
REWARD_SCALAR = False
DISCRETE_ACTION = False

'''
    train related
'''
# TRAIN_STRATEGY = 'Random'
TRAIN_STRATEGY = 'Divergence'
NUM_EPISODE = 1000
UPPER_LIMIT = 2000
MIXED_SAMPLE = False
USE_Q_MOD = False
Q_MOD_RATE = [1, 1]
TEST_RATE = 1.0
COMPUTE_REWARD = True
BOTH_GOOD_ACTION = False
TRAIN_NETWORK = True
TEST_POSITIVE_NETWORK = True
TEST_NEGATIVE_NETWORK = True
TEST_MIXED_NETWORK = True

'''
    network related
'''
ALGORITHM_NAME = 'ac_continuous'  # dqn\ddqn\ac\ac_continuous
ALGORITHM_TYPE = 'new_algo_2'  # classic\new_algo_1\new_algo_2
MEMORY_CAPACITY = 100000
START_LEARN_STEP = 0
BATCH_SIZE = 32
BIDIRECTION = False
LR_POSITIVE = 0.001
LR_NEGATIVE = 0.001
REWARD_DECAY_POSITIVE = 0.9
REWARD_DECAY_NEGATIVE = 0.9
E_GREEDY_POSITIVE = 0.95
E_GREEDY_NEGATIVE = 0.95
FC_NODE = 128
REPLACE_TARGET_ITER = 0
FINAL_ITER = 1000
E_GREEDY_INCREMENT = None
PG_LEARNING_RATE = 0.001
PG_DECAY_RATE = 0.99
RENDER = False  # rendering wastes time
GAMMA_C0 = 0.9     # reward discount in TD error
GAMMA_C1 = 0.9
LR_A = 0.0001    # learning rate for actor
LR_C0 = 0.001    # learning rate for critic0
LR_C1 = 0.001

'''
    date related
'''
SAVE_DATA = False
DATA_DIR = '/data/'
OUTPUT_FILE_POSITIVE = DATA_DIR + ALGORITHM_NAME + '/' + ALGORITHM_NAME + '-positive.npy'
OUTPUT_FILE_NEGATIVE = DATA_DIR + ALGORITHM_NAME + '/' + ALGORITHM_NAME + '-negative.npy'
OUTPUT_FILE_MIXED = DATA_DIR + ALGORITHM_NAME + '/' + ALGORITHM_NAME + '-mix.npy'
