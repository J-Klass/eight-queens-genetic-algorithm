import matplotlib.pyplot as plt
import numpy as np


def show(positions):
    board = np.zeros((8, 8, 3))
    board += 0.5
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1

    positions = [x - 1 for x in positions]

    fig, ax = plt.subplots()
    ax.imshow(board, interpolation="nearest")

    queen = plt.imread("eight_queens/resources/queen.png")
    extent = np.array([-0.4, 0.4, -0.4, 0.4])
    for y, x in enumerate(positions):
        ax.imshow(queen, extent=extent + [x, x, y, y])

    ax.set(xticks=[], yticks=[])
    ax.axis("image")

    plt.show()
