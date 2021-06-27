"""
@author: M.K
different types of initial lattices
"""
import numpy as np


def two_stripes(N):
    """

    :param N:
    :return:
    """
    n = N // 2
    a = -np.ones((N, n))
    b = np.ones((N, N - n))
    return np.concatenate((a, b), axis=1)


def diagonal_stripes(N):
    """

    :param N:
    :return:
    """
    vec = np.linspace(-1.5, 1.5, N)
    array1 = np.repeat(vec[None], N, axis=0)
    array2 = np.repeat(vec[None].T, N, axis=1)
    array = np.zeros((N, N)) - 1
    array[np.logical_and(array2 < 1 - array1, array2 > -1 - array1)] = 1
    return array


def circle(N):
    """

    :param N:
    :return:
    """
    vec = np.linspace(-1.5, 1.5, N)
    array1 = np.repeat(vec[None], N, axis=0)
    array2 = np.repeat(vec[None].T, N, axis=1)
    array = np.zeros((N, N)) - 1
    array[array1 ** 2 + array2 ** 2 <= 1] = 1
    return array


def ring(N):
    """

    :param N:
    :return:
    """
    vec = np.linspace(-1.5, 1.5, N)
    array1 = np.repeat(vec[None], N, axis=0)
    array2 = np.repeat(vec[None].T, N, axis=1)
    array = np.zeros((N, N)) - 1
    array[np.logical_and(array1 ** 2 + array2 ** 2 <= 1, array1 ** 2 + array2 ** 2 >= 0.8)] = 1
    return array


def chessboard(N):
    """

    :param N:
    :return:
    """
    return 2 * (np.indices([N, N]).sum(axis=0) % 2) - 1


def random_lattice(N):
    """

    :param N:
    :return:
    """
    return np.random.choice([-1, 1], (N, N))


def solid(N):
    """

    :param N:
    :return:
    """
    return np.ones((N, N))
