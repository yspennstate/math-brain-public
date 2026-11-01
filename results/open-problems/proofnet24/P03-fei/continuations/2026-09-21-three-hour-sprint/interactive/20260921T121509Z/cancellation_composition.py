"""Independent FEI cancellation-composition calculations.

Convention: Boolean values +/-1; 'true' is -1. Each reused child below
means a fresh disjoint copy, never shared variables. Float routines are
exploratory; integer Walsh transforms validate finite examples exactly
before logarithms are evaluated. No routine certifies full FEI.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


def phi(x: float) -> float:
    return -x * math.log2(x) if x > 0 else 0.0


@dataclass(frozen=True)
class State:
    p: float
    influence: float
    nonempty_entropy: float
    nonempty_cancellation: float
    leaves: int

    @property
    def empty_mass(self) -> float:
        return (1 - 2 * self.p) ** 2

    @property
    def variance(self) -> float:
        return 4 * self.p * (1 - self.p)

    @property
    def empty_entropy(self) -> float:
        v = self.variance
        return -(1-v)*math.log1p(-v)/math.log(2) if v < 1 else 0.0

    @property
    def entropy(self) -> float:
        return self.nonempty_entropy + self.empty_entropy

    @property
    def cancellation(self) -> float:
        return self.nonempty_cancellation + self.empty_entropy

    def negate(self) -> State:
        return State(1-self.p, self.influence, self.nonempty_entropy,
                     self.nonempty_cancellation, self.leaves)

    def as_dict(self) -> dict:
        i = self.influence
        return {'p': self.p, 'I': i, 'H': self.entropy,
                'Bcan': self.cancellation,
                'H_over_I': self.entropy/i if i else None,
                'Bcan_over_I': self.cancellation/i if i else None,
                'leaves': self.leaves}


def variable() -> State:
    return State(0.5, 1.0, 0.0, 0.0, 1)


def and_state(a: State, b: State) -> State:
    p, q = a.p, b.p
    va, vb = a.variance, b.variance
    # q^2 log(1/q) has its continuous value zero at q=0.
    r = q*phi(q)*va + p*phi(p)*vb
    return State(p*q,
                 q*a.influence + p*b.influence,
                 q*a.nonempty_entropy + p*b.nonempty_entropy + 2*r + va*vb/2,
                 q*a.nonempty_cancellation + p*b.nonempty_cancellation + r,
                 a.leaves+b.leaves)


def or_state(a: State, b: State) -> State:
    return and_state(a.negate(), b.negate()).negate()


def fwht(values: np.ndarray) -> np.ndarray:
    a = np.asarray(values, dtype=np.int64).copy()
    n = len(a)
    if n == 0 or n & (n-1):
        raise ValueError('Length must be a positive power of two')
    h = 1
    while h < n:
        b = a.reshape(-1, 2*h)
        x, y = b[:, :h].copy(), b[:, h:].copy()
        b[:, :h], b[:, h:] = x+y, x-y
        h *= 2
    return a


def walsh_state(values: np.ndarray) -> State:
    v = np.asarray(values, dtype=np.int64)
    if not np.all((v == 1) | (v == -1)):
        raise ValueError('The truth table must be Boolean +/-1')
    N = len(v)
    n = N.bit_length()-1
    W = fwht(v)
    sq = W*W
    if int(sq.sum()) != N*N:
        raise AssertionError('Parseval check failed')
    # Integer upper zeta transform: each intermediate value <= N^2.
    ups = sq.copy()
    for k in range(n):
        h = 1 << k
        u = ups.reshape(-1, 2*h)
        u[:, :h] += u[:, h:]
    non = sq[1:] > 0
    pm = sq[1:][non]/(N*N)
    E = float(np.sum(-pm*np.log2(pm)))
    T = float(np.sum(pm*np.log2(ups[1:][non]/sq[1:][non])))
    I = sum(s.bit_count()*int(sq[s]) for s in range(N))/(N*N)
    return State(float(np.count_nonzero(v == -1)/N), I, E, T, n)


def and_table(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    # Cartesian product inputs; all copies independent.
    return np.where((a[:, None] == -1) & (b[None, :] == -1), -1, 1).ravel()


def random_formula(n: int, rng: np.random.Generator) -> tuple[State, np.ndarray, str]:
    if n == 1:
        return variable(), np.array([1, -1], dtype=np.int64), 'x'
    k = int(rng.integers(1, n))
    a, at, astr = random_formula(k, rng)
    b, bt, bstr = random_formula(n-k, rng)
    if rng.integers(2):
        a, at, astr = a.negate(), -at, f'!({astr})'
    if rng.integers(2):
        b, bt, bstr = b.negate(), -bt, f'!({bstr})'
    return and_state(a, b), and_table(at, bt), f'({astr}&{bstr})'


def validate(seed: int = 20260921, trials: int = 360) -> dict:
    rng = np.random.default_rng(seed)
    maxerr = np.zeros(4)
    for j in range(trials):
        n = 2 + j % 11
        s, table, _ = random_formula(n, rng)
        t = walsh_state(table)
        err = np.abs(np.array([s.p-t.p, s.influence-t.influence,
                             s.entropy-t.entropy, s.cancellation-t.cancellation]))
        maxerr = np.maximum(maxerr, err)
        if np.max(err) > 5e-12:
            raise AssertionError((n, s, t, err))
    return {'seed': seed, 'random_disjoint_formulas': trials,
            'dimensions': [2, 12], 'max_absolute_errors_p_I_H_Bcan': maxerr.tolist(),
            'spectral_coefficients_and_upsets': 'integer exact',
            'logarithms': 'float64 exploratory cross-check'}


if __name__ == '__main__':
    import json
    print(json.dumps(validate(), indent=2))
    s = variable()
    out = []
    for n in range(2, 65):
        s = and_state(s, variable())
        if n in [2,3,4,8,16,32,64]: out.append(s.as_dict())
    print(json.dumps(out, indent=2))
