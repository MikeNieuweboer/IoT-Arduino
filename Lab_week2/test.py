import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def get_rot_matrix(angle):
    return np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])

def get_pixel(img, coord):
    x, y = coord
    if y < 0 or y >= len(img) or x < 0 or x >= len(img[y]):
        return np.array((0, 0, 0))
    return img[y][x]

cap = cv2.VideoCapture(0)

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
output = np.zeros((height, width, 3))

angle = math.pi / 7

rot_matrix = get_rot_matrix(-angle)

succes, img = cap.read()
if not succes:
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

for y, column in enumerate(output):
    for x, _ in enumerate(column):
        old_coords = np.matmul(rot_matrix, np.array([[x - width / 2], [y - height / 2]]))
        old_coords += np.array([[width / 2], [height / 2]])
        old_coords.resize(2,)
        old_x, old_y = old_coords

        x1 = math.floor(old_x)
        x2 = x1 + 1
        y1 = math.floor(old_y)
        y2 = y1 + 1

        w11 = (x2 - old_x) * (y2 - old_y)
        w12 = (x2 - old_x) * (old_y - y1)
        w21 = (old_x - x1) * (y2 - old_y)
        w22 = (old_x - x1) * (old_y - y1)

        pixel = (
            w11 * get_pixel(img, (x1, y1))
            + w12 * get_pixel(img, (x1, y2))
            + w21 * get_pixel(img, (x2, y1))
            + w22 * get_pixel(img, (x2, y2))
        )

        output[y][x] = pixel / 255

plt.imshow(output)
plt.show()
