"""
Functions for error checking.
"""

def is_positive_integer(L):
    if not isinstance(L, int) or L < 0:
        raise ValueError(f'lattice size must be a positive integer - {L} given')
    
def is_probability(p):
    if not isinstance(p, float) or p < 0 or p > 1:
        raise ValueError(f'probabilty must be a float between 0 and 1 - given {p}')
    
def is_bool(var):
    if not isinstance(var, bool):
        raise ValueError(f'variable must be boolean - {var} given')
    
def is_proper_q(q):
    if q > 4 and not isinstance(q, int):
        raise ValueError(f'q must be at most 4 - {q} given')    
