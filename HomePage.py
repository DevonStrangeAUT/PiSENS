from sense_hat import SenseHat

sense = SenseHat()

R = (255,0,0)
B = (0,0,255)
W = (255,255,255)
G = (0, 255,0)

house = [
    B, B, B, W, W, B, B, B,
    B, B, W, B, B, W, B, B,
    B, W, B, B, B, B, W, B,
    W, W, W, B, B, W, W, W,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    G, G, W, B, B, W, G, G,
    G, G, W, W, W, W, G, G
]

sense.set_pixels(house)