#!/usr/bin/env python3
"""Exact checker for B16 pair-correlation/Shapley curvature bridge.

Standard-library only.  All game identities use fractions.Fraction.
"""
from fractions import Fraction
from itertools import product
from math import factorial
import json
import random

SEED = 160921
rng = random.Random(SEED)

def subsets(items):
    items = tuple(items)
    for bits in product((0, 1), repeat=len(items)):
        yield frozenset(x for x, b in zip(items, bits) if b)

def beta_int(a, b):
    # integral_0^1 t^a (1-t)^b dt
    return Fraction(factorial(a) * factorial(b), factorial(a + b + 1))

def shapley_player(V, players, a):
    n = len(players)
    others = [p for p in players if p != a]
    out = Fraction(0)
    for R in subsets(others):
        k = len(R)
        w = Fraction(factorial(k) * factorial(n-k-1), factorial(n))
        out += w * (V[R | {a}] - V[R])
    return out

def fine_pair_share(V, m, j):
    players = list(range(2*m))
    return shapley_player(V, players, 2*j) + shapley_player(V, players, 2*j+1)

def complete_pairs(pair_set):
    out = set()
    for k in pair_set:
        out.update((2*k, 2*k+1))
    return frozenset(out)

def coarse_pair_share(V, m, j):
    others = [k for k in range(m) if k != j]
    out = Fraction(0)
    for A in subsets(others):
        k = len(A)
        w = Fraction(factorial(k) * factorial(m-k-1), factorial(m))
        R = complete_pairs(A)
        out += w * (V[R | {2*j, 2*j+1}] - V[R])
    return out

def bridge_rhs(V, m, j):
    """Exact RHS of Theorem 1, integrated using beta integrals."""
    a, b = 2*j, 2*j+1
    target = {a, b}
    other_players = [p for p in range(2*m) if p not in target]
    q = len(other_players)

    # int E_ind,t Delta_{P_j} V dt
    independent_block = Fraction(0)
    # int (1-2t) E_ind,t Delta_a Delta_b V dt
    target_curvature = Fraction(0)
    for R in subsets(other_players):
        r = len(R)
        w = beta_int(r, q-r)
        block_delta = V[R | target] - V[R]
        independent_block += w * block_delta

        w1 = w - 2 * beta_int(r+1, q-r)
        pair_delta = V[R | target] - V[R | {a}] - V[R | {b}] + V[R]
        target_curvature += w1 * pair_delta

    # int E_coupled,t Delta_{P_j} V dt
    other_pairs = [k for k in range(m) if k != j]
    coupled_block = Fraction(0)
    for A in subsets(other_pairs):
        k = len(A)
        w = beta_int(k, len(other_pairs)-k)
        R = complete_pairs(A)
        coupled_block += w * (V[R | target] - V[R])

    return independent_block - coupled_block - target_curvature

def pair_state_subset(states, pair_indices):
    R = set()
    for k, state in zip(pair_indices, states):
        if state & 1:
            R.add(2*k)
        if state & 2:
            R.add(2*k+1)
    return frozenset(R)

def pair_probs(t, lam):
    s = t * (1-t)
    return {
        0: (1-t)*(1-t) + lam*s, # 00
        1: (1-lam)*s,           # 10
        2: (1-lam)*s,           # 01
        3: t*t + lam*s,         # 11
    }

def expectation_pair_correlation(F, pair_indices, t, lam):
    probs = pair_probs(t, lam)
    out = Fraction(0)
    for states in product(range(4), repeat=len(pair_indices)):
        p = Fraction(1)
        for state in states:
            p *= probs[state]
        out += p * F(pair_state_subset(states, pair_indices))
    return out

def correlation_derivative_rhs(F, pair_indices, t, lam):
    """t(1-t) sum_k E Delta_{k0}Delta_{k1} F."""
    probs = pair_probs(t, lam)
    total = Fraction(0)
    for k in pair_indices:
        rest = [h for h in pair_indices if h != k]
        for states in product(range(4), repeat=len(rest)):
            p = Fraction(1)
            for state in states:
                p *= probs[state]
            R = pair_state_subset(states, rest)
            x, y = 2*k, 2*k+1
            delta = F(R | {x, y}) + F(R) - F(R | {x}) - F(R | {y})
            total += p * delta
    return t * (1-t) * total

def pair_complete_biased_coefficient(F, pair_indices, t, A):
    """p-biased orthonormal coefficient on both clone bits of each pair in A.

    The square roots cancel because |P_A|=2|A|:
      hat F(P_A)=E[F prod_{i in P_A}(X_i-t)]/[t(1-t)]^{|A|}.
    """
    out = Fraction(0)
    for states in product(range(4), repeat=len(pair_indices)):
        R = pair_state_subset(states, pair_indices)
        r = len(R)
        prob = (t**r) * ((1-t)**(2*len(pair_indices)-r))
        centered = Fraction(1)
        for k in A:
            for p in (2*k, 2*k+1):
                centered *= (Fraction(1 if p in R else 0) - t)
        out += prob * F(R) * centered
    if not A:
        return out
    return out / ((t*(1-t))**len(A))

def spectral_derivative(F, pair_indices, t, lam):
    total = Fraction(0)
    for A in subsets(pair_indices):
        if A:
            coeff = pair_complete_biased_coefficient(F, pair_indices, t, A)
            total += len(A) * (lam**(len(A)-1)) * coeff
    return total

def random_game(m):
    players = list(range(2*m))
    return {
        S: Fraction(rng.randint(-7, 7), rng.randint(1, 7))
        for S in subsets(players)
    }

def harsanyi_game(m, max_degree):
    """Random exact game built from dividends up to max_degree."""
    players = list(range(2*m))
    div = {}
    for T in subsets(players):
        if len(T) <= max_degree:
            div[T] = Fraction(rng.randint(-5, 5), rng.randint(1, 5))
    V = {}
    for S in subsets(players):
        V[S] = sum((d for T, d in div.items() if T <= S), Fraction(0))
    return V

def signed_parity_game(m):
    players = list(range(2*m))
    R = frozenset(p for p in players if rng.randrange(2))
    if not R:
        R = frozenset({rng.choice(players)})
    c = Fraction(rng.choice((-5,-3,-1,1,2,4,7)), rng.randint(1,5))
    return {
        S: c * Fraction(1 - (-1)**len(S & R), 2)
        for S in subsets(players)
    }

def check_game(V, m):
    checks = 0
    for j in range(m):
        lhs = fine_pair_share(V, m, j) - coarse_pair_share(V, m, j)
        rhs = bridge_rhs(V, m, j)
        assert lhs == rhs, (m, j, lhs, rhs)
        checks += 1
    return checks

def main():
    counts = {
        "general_bridge_identities": 0,
        "signed_parity_bridge_identities": 0,
        "degree_le_2_zero_defect_checks": 0,
        "correlation_derivative_checks": 0,
        "pair_spectral_diagonalization_checks": 0,
        "generic_endpoint_l2_obstruction_checks": 0,
    }

    # General exact games.
    for m, trials in ((2, 40), (3, 32), (4, 12)):
        for _ in range(trials):
            V = random_game(m)
            counts["general_bridge_identities"] += check_game(V, m)

    # Signed parity games retain either sign.
    for m, trials in ((2, 40), (3, 40), (4, 20)):
        for _ in range(trials):
            V = signed_parity_game(m)
            counts["signed_parity_bridge_identities"] += check_game(V, m)

    # The refinement defect must vanish for all games of Harsanyi degree <=2.
    for m, trials in ((2, 25), (3, 25), (4, 10)):
        for _ in range(trials):
            V = harsanyi_game(m, 2)
            for j in range(m):
                defect = fine_pair_share(V, m, j) - coarse_pair_share(V, m, j)
                assert defect == 0, (m, j, defect)
                counts["degree_le_2_zero_defect_checks"] += 1

    # Exact correlation-flow derivative and p-biased pair-parity diagonalization.
    sample_t = (Fraction(1,5), Fraction(2,5), Fraction(1,2), Fraction(3,5), Fraction(4,5))
    sample_lam = (Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1))
    for m, trials in ((3, 18), (4, 8)):
        for _ in range(trials):
            j = rng.randrange(m)
            pair_indices = [k for k in range(m) if k != j]
            other_players = [p for k in pair_indices for p in (2*k, 2*k+1)]
            values = {
                S: Fraction(rng.randint(-6,6), rng.randint(1,6))
                for S in subsets(other_players)
            }
            F = lambda R, values=values: values[R]
            for t in sample_t:
                for lam in sample_lam:
                    # spectral diagonalization
                    lhs = expectation_pair_correlation(F, pair_indices, t, lam)
                    rhs = Fraction(0)
                    for A in subsets(pair_indices):
                        rhs += (lam**len(A)) * pair_complete_biased_coefficient(
                            F, pair_indices, t, A
                        )
                    assert lhs == rhs, ("spectral", m, j, t, lam, lhs, rhs)
                    counts["pair_spectral_diagonalization_checks"] += 1

                    # derivative, represented both spectrally and by pair second differences
                    lhs_d = spectral_derivative(F, pair_indices, t, lam)
                    rhs_d = correlation_derivative_rhs(F, pair_indices, t, lam)
                    assert lhs_d == rhs_d, ("derivative", m, j, t, lam, lhs_d, rhs_d)
                    counts["correlation_derivative_checks"] += 1

    # Generic endpoint-L2 obstruction: at t=1/2, complete-pair parity modes
    # can add coherently at lambda=1. This is a game-level obstruction only,
    # not an entropy-game or FEI counterexample.
    for q in range(1, 7):
        m = q + 1
        j = q
        pair_indices = list(range(q))
        def F_obstruct(R, pair_indices=pair_indices):
            # prod_k (1 + parity_k) - 1, where parity_k=(2X_0-1)(2X_1-1)
            val = 1
            for k in pair_indices:
                x0 = 1 if 2*k in R else 0
                x1 = 1 if 2*k+1 in R else 0
                parity = (2*x0-1)*(2*x1-1)
                val *= (1 + parity)
            return Fraction(val - 1)
        t = Fraction(1,2)
        e0 = expectation_pair_correlation(F_obstruct, pair_indices, t, Fraction(0))
        e1 = expectation_pair_correlation(F_obstruct, pair_indices, t, Fraction(1))
        assert e0 == 0
        assert e1 == 2**q - 1
        coeff_sq = Fraction(0)
        for A in subsets(pair_indices):
            if A:
                c = pair_complete_biased_coefficient(F_obstruct, pair_indices, t, A)
                assert c == 1
                coeff_sq += c*c
        assert coeff_sq == 2**q - 1
        counts["generic_endpoint_l2_obstruction_checks"] += 1

    out = {
        "status": "PASS",
        "arithmetic": "fractions.Fraction exact rational",
        "seed": SEED,
        "counts": counts,
        "total_exact_checks": sum(counts.values()),
        "claims_checked": [
            "ordinary fine Shapley pair aggregate minus block-coupled/coarse Shapley equals the two-term pair-correlation curvature bridge",
            "pair-correlation interpolation derivative is t(1-t) times the summed within-pair second difference",
            "the interpolation diagonalizes exactly on complete pair-parity p-biased Fourier modes with eigenvalue lambda^|A|",
            "all Harsanyi-degree <=2 games have zero refinement defect",
            "signed parity games satisfy the same identities for either coefficient sign",
            "generic endpoint lambda=1 pair-correlation evaluation has no dimension-free L2 bound (explicit complete-pair parity family)",
        ],
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
