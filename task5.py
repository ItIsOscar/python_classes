import numpy as np
from matplotlib import pyplot as plt
_STOP_INTERVAL_SECONDS = 0.1
_START_POPULARITY = 0.3
_WIDTH = 200
_HEIGHT = 200
_LIVE_CND = {3}
_DYING_CND = {0, 1, 4, 5, 6, 7, 8}
field_state = np.random.random((_HEIGHT, _WIDTH))
mask = (field_state < _START_POPULARITY)
field_state[...][mask] = 1
field_state[...][mask == False] = 0

def sumNeightors(y, x):
    return np.sum(field_state[max(0, y - 1):min(y + 2, _HEIGHT), max(0, x - 1):min(x + 2, _WIDTH)], dtype=np.int8) - field_state[y][x]

def nextFrame():
    return np.array([[1 if (
        (field_state[y][x] or sumNeightors(y, x) in _LIVE_CND) and not (sumNeightors(y, x) in _DYING_CND)) else 0
                      for x in range(0, _WIDTH)] for y in range(0, _HEIGHT)])

next_field_state = nextFrame()
while True:
    plt.imshow(field_state, cmap = plt.cm.gray)
    plt.pause(_STOP_INTERVAL_SECONDS)
    field_state = next_field_state
    next_field_state = nextFrame()
    if np.array_equal(field_state, np.zeros((_HEIGHT, _WIDTH))) or np.array_equal(field_state, next_field_state):
        break

