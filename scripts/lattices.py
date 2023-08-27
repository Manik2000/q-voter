"""
Different types of initial lattices.
"""
import numpy as np


def two_vertical_stripes(N: int):
    lattice = np.ones((N, N))
    lattice[:, :N//2] = -1
    return lattice


def diagonal_stripes(N: int):
    vec = np.linspace(-1.5, 1.5, N)
    X, Y = np.meshgrid(vec, vec)
    array = np.zeros((N, N)) - 1
    array[np.logical_and(Y < 1 - X, Y > -1 - X)] = 1
    return array


def circle(N: int):
    vec = np.linspace(-1.5, 1.5, N)
    X, Y = np.meshgrid(vec, vec)
    array = np.zeros((N, N)) - 1
    array[X ** 2 + Y ** 2 <= 1] = 1
    return array


def ring(N: int):
    vec = np.linspace(-1.5, 1.5, N)
    X, Y = np.meshgrid(vec, vec)
    array = np.zeros((N, N)) - 1
    array[np.logical_and(X ** 2 + Y ** 2 <= 1, X ** 2 + Y ** 2 >= 0.8)] = 1
    return array


def chessboard(N: int):
    return 2 * (np.indices([N, N]).sum(axis=0) % 2) - 1


def random_lattice(N: int):
    return np.random.choice([-1, 1], (N, N))


def solid(N: int):
    return np.ones((N, N))
