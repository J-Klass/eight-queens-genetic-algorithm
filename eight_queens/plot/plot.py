import json

import matplotlib.pyplot as plt
import numpy as np

with open("eight_queens/configurations.json") as json_file:
    data = json.load(json_file)
    NUMBER_OF_QUEENS = data["number_of_queens"]


def plot(positions):
    """ Plot the chessboard

    :param positions: positions where the queens are placed
    :return: nones
    """
    board = np.zeros((NUMBER_OF_QUEENS, NUMBER_OF_QUEENS, 3))
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
