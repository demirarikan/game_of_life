import matplotlib.pyplot as plt
import numpy as np
import sys

HEIGHT = 128
WIDTH = 128

plt.ion()
fig = plt.figure()
probabilities = [0.9, 0.1]
grid = np.random.choice([0, 1], size=(HEIGHT, WIDTH), p=probabilities)

try:
    while True:
        new_grid = grid.copy()
        ax = fig.add_subplot(111)
        ax.matshow(grid)
        plt.draw()
        plt.pause(1)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                left = (x - 1) % WIDTH
                right = (x + 1) % WIDTH
                up = (y - 1) % HEIGHT
                down = (y + 1) % HEIGHT

                num_neighbor = 0
                if grid[left, down] > 0:
                    num_neighbor += 1
                if grid[left, y] > 0:
                    num_neighbor += 1
                if grid[left, up] > 0:
                    num_neighbor += 1
                if grid[x, up] > 0:
                    num_neighbor += 1
                if grid[x, down] > 0:
                    num_neighbor += 1
                if grid[right, down] > 0:
                    num_neighbor += 1
                if grid[right, y] > 0:
                    num_neighbor += 1
                if grid[right, up] > 0:
                    num_neighbor += 1

                if grid[x, y] == 1 :
                    if num_neighbor < 2 or num_neighbor > 3:
                        new_grid[x, y] = 0
                if grid[x, y] == 0:
                    if num_neighbor == 3:
                        new_grid[x, y] = 1
        grid = new_grid
except KeyboardInterrupt:
    print('STOPPING...')
    sys.exit()
