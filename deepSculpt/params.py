from tensorflow.random import normal

## TRAINING PARAMS

LOCALLY = False

CREATE_DATA = False

N_SAMPLES = 10

VOID_DIM = 24

BUFFER_SIZE = 160

BATCH_SIZE = 16

EPOCHS = 80

NOISE_DIM = 512

SCULPTS_GEN = 1

SEED = normal([SCULPTS_GEN, NOISE_DIM])

BUCKET_NAME = "deepsculpt"

BUCKET_TRAIN_DATA_PATH = "data"

MODEL_BASE_PATH = ""

## ELEMENTS PARAMS

N_EDGE_ELEMENTS = 2

N_PLANE_ELEMENTS = 2

N_VOLUME_ELEMENTS = 2

COLOR_EDGES = "dimgrey"

COLOR_PLANES = "snow"

COLOR_VOLUMES = ["crimson", "turquoise", "gold"]

"""[
        "crimson", "turquoise", "gold", "orange", "mediumpurple", "greenyellow",
        "firebrick", "salmon", "coral", "chartreuse", "steelblue", "lavender", "royalblue",
        "indigo", "mediumvioletred"
    ]"""

ELEMENT_EDGE_MIN, ELEMENT_EDGE_MAX = int(VOID_DIM * 0.8), int(VOID_DIM * 0.9)

ELEMENT_GRID_MIN, ELEMENT_GRID_MAX = int(VOID_DIM * 0.8), int(VOID_DIM * 0.95)

ELEMENT_PLANE_MIN, ELEMENT_PLANE_MAX = int(VOID_DIM * 0.4), int(VOID_DIM * 0.8)

ELEMENT_VOLUME_MIN, ELEMENT_VOLUME_MAX = int(VOID_DIM * 0.2), int(VOID_DIM * 0.5)

STEP = 1

VERBOSE = False
