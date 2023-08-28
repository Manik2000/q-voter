"""
Functions performing Q-voter model simluations.
There are two variants of the model: independence and anti-conformity.
"""
import numpy as np

from scripts.checkers import *


def independence(lattice: np.ndarray, L: int, replacement: bool, q: int, p: float, f:float) -> np.ndarray:
    """
    Simulate the independence q-voter model on a square lattice.
    :param lattice: lattice with agents (np.array)
    :param L: size of the lattice (int)
    :param replacement: specifies if drawings are with or without replacement (boolean)
    :param q: the number of drawn neighbours (int)
    :param p: the probability of independence (float)
    :param f: probability of spin-flip if independence (float)
    :return: final lattice with agents after L steps (np.ndarray)
    """
    is_positive_integer(L)
    is_probability(p)
    is_probability(f)
    is_bool(replacement)
    is_proper_q(q)
    for _ in range(L):
        i, j = np.random.randint(0, L, 2)
        agent = lattice[i][j]
        U = np.random.rand()
        if U < p:
            if np.random.rand() < f:
                lattice[i][j] = -agent
        else:
            neighbours = [lattice[i][(j + 1) % L], lattice[i][(j - 1) % L],
                          lattice[(i + 1) % L][j], lattice[(i - 1) % L][j]]
            if replacement:
                indexes = np.random.randint(0, 3, size=q)
                chosen = [neighbours[i] for i in indexes]
            else:
                indexes = []
                while len(indexes) < q:
                    new = np.random.randint(0, 4)
                    if new not in indexes:
                        indexes.append(new)
                chosen = [neighbours[i] for i in indexes]
            if sum(chosen) == q or sum(chosen) == -q:
                lattice[i][j] = chosen[0]
    return lattice


def anti_conformity(lattice: np.ndarray, L: int, replacement: bool, q: int, p:float) -> np.ndarray:
    """
    Simulate the anti-conformity q-voter model on a square lattice.
    :param lattice: lattice with agents (np.ndarray)
    :param L: size of the lattice (int)
    :param replacement: specifies if drawings are with or without replacement (boolean)
    :param q: the number of drawn neighbours (int)
    :param p: the probability of anti-conformity (float)
    :return: the lattice after transitions (np.ndarray)
    """
    is_positive_integer(L)
    is_probability(p)
    is_bool(replacement)
    is_proper_q(q)
    for _ in range(L):
        i, j = np.random.randint(0, L, 2)
        neighbours = [lattice[i][(j + 1) % L], lattice[i][(j - 1) % L], 
                      lattice[(i + 1) % L][j], lattice[(i - 1) % L][j]]
        if replacement:
            indexes = np.random.randint(0, 3, q)
            chosen = [neighbours[i] for i in indexes]
        else:
            indexes = []
            while len(indexes) < q:
                new = np.random.randint(0, 4)
                if new not in indexes:
                    indexes.append(new)
            chosen = [neighbours[i] for i in indexes]
        U = np.random.rand()
        if U < p:  # anti-conformity
            if sum(chosen) == q or sum(chosen) == -q:
                lattice[i][j] = -chosen[0]
        else:  # conformity
            if sum(chosen) == q or sum(chosen) == -q:
                lattice[i][j] = chosen[0]
    return lattice
