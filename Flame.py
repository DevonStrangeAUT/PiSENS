from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

BLACK  = [0, 0, 0]
RED    = [255, 0, 0]
ORANGE = [255, 120, 0]
YELLOW = [255, 200, 0]

def flicker(color):
    """Randomly adjust brightness for flicker effect."""
    flick = random.randint(-40, 30)
    return [max(0, min(255, c + flick)) for c in color]

def flame_pattern():
    """Return an 8x8 flame-like pixel pattern."""
    # Base flame shape (0 = off, 1 = red, 2 = orange, 3 = yellow)
    shape = [
        [0,0,0,3,3,0,0,0],
        [0,0,3,3,3,3,0,0],
        [0,3,3,3,3,3,3,0],
        [0,3,3,2,2,3,3,0],
        [0,1,2,2,2,2,1,0],
        [0,1,1,2,2,1,1,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0]
    ]

    # Convert shape to color pixels with flicker
    pixels = []
    for y in range(8):
        for x in range(8):
            val = shape[y][x]
            if val == 1:
                pixels.append(flicker(RED))
            elif val == 2:
                pixels.append(flicker(ORANGE))
            elif val == 3:
                pixels.append(flicker(YELLOW))
            else:
                # occasional black flicker for realism
                if random.random() < 0.05:
                    pixels.append(flicker(RED))
                else:
                    pixels.append(BLACK)
    return pixels

try:
    while True:
        sense.set_pixels(flame_pattern())
        sleep(0.1)
except KeyboardInterrupt:
    sense.clear()