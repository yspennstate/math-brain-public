"""Referee check of W-N61 (Proposition 6.1) on the family F_{D,w}.

(1) exact truth-table spectrum for small (D, w): only phi-set {x_0}, its mass (1-2d)^2, v = 1, I(F) formula;
(2) the single-root cost of A = {x_0} in every gate, with the exact normalizer Z_1, for every lambda on a fine grid,
    giving the proof's lower bound  RHS >= (1-2d)^2 * min_l C({x0}) + Lambda_lambda  (t < 1), and the t >= 1 bound;
    the minimum over lambda is compared with (1-2d)^2 (D/2 + 2);
(3) the scale-mixture bracket for {x_0}, min over lambda of Lambda_lambda + C_lambda({x0}) (weights only add);
(4) log(1/Q_lb({x_0})) with all 2^{D+1} single-root witnesses (exact Z_1), against 7.21;
(5) the complemented representation (gates kappa AND [g = -1]).
"""
import math
from fractions import Fraction
import numpy as np
from rc_common import coords, spectrum, popcount, bits_of, LOG2E

a = 1.2


def build_F(D, w):
    """Variables: x0 = 0; plus-side internal nodes, minus-side internal nodes (heap order), then data blocks."""
    n_int = (1 << D) - 1
    n = 1 + 2 * n_int + (1 << (D + 1)) * w
    X = coords(n)
    out = np.zeros(1 << n, dtype=np.int8)

    def side(base_var, base_data, kind):
        # complete tree in heap order: node k (0-based) has var base_var+k, children 2k+1, 2k+2; leaves 0..2^D-1
        res = np.zeros(1 << n, dtype=np.int8)
        leaf_idx = np.zeros(1 << n, dtype=np.int64)
        for k in range(D):
            pass
        # walk: compute leaf index from the D node variables along the path
        node = np.zeros(1 << n, dtype=np.int64)
        for depth in range(D):
            bit = (X[0] * 0 + 0)
            var_of_node = base_var + node
            # x value at the current node for every input
            xv = np.empty(1 << n, dtype=np.int8)
            for k in np.unique(node):
                m = node == k
                xv[m] = X[base_var + int(k)][m]
            node = np.where(xv == 1, 2 * node + 1, 2 * node + 2)
        leaf = node - n_int  # 0..2^D-1
        for L in range(1 << D):
            m = leaf == L
            vals = np.ones(int(m.sum()), dtype=np.int64) * 0
            ys = [X[base_data + L * w + j][m].astype(np.int64) for j in range(w)]
            ssum = sum(ys)
            if kind == 'or':
                res[m] = np.where(ssum > -w, 1, -1)
            else:
                res[m] = np.where(ssum == w, 1, -1)
        return res

    plus = side(1, 1 + 2 * n_int, 'or')
    minus = side(1 + n_int, 1 + 2 * n_int + (1 << D) * w, 'and')
    out = np.where(X[0] == 1, plus, minus).astype(np.int8)
    return n, out


def exact_spectrum_check():
    rows = []
    for D, w in [(1, 2), (1, 3), (2, 2), (1, 4), (2, 3)]:
        if 1 + 2 * ((1 << D) - 1) + (1 << (D + 1)) * w > 23:   # size guard BEFORE building (memory)
            continue
        n, f = build_F(D, w)
        nn, spec = spectrum(f)
        N = 1 << n
        den = Fraction(1, N * N)
        dl = Fraction(1, 1 << w)
        v = sum((c * c * den for S, c in spec.items() if S != 0), Fraction(0))
        I = sum((popcount(S) * c * c * den for S, c in spec.items() if S != 0), Fraction(0))
        ctrl_mask = (1 << (1 + 2 * ((1 << D) - 1))) - 1
        phis = [(S, c) for S, c in spec.items() if S != 0 and (S & ~ctrl_mask) == 0]
        I_pred = (1 - 2 * dl) ** 2 + 2 * dl * (1 - dl) * (D + 1) + 2 * w * dl
        ok = (v == 1 and I == I_pred and len(phis) == 1 and phis[0][0] == 1
              and phis[0][1] * phis[0][1] * den == (1 - 2 * dl) ** 2)
        rows.append((D, w, n, ok, float(I)))
    return rows


def Z1(D, w):
    return sum(r ** -a for r in range(1, D + 2)) + sum(r ** -a for r in range(1, w + 1))


def lam_grid():
    return [2.0 ** (k / 8.0) for k in range(-8 * 40, 8 * 80)]


def lower_bound_scan(D, w, complemented=False):
    dl = 2.0 ** (-w)
    # pi of the plus-side gates and minus-side gates
    if not complemented:
        pi_plus = (1 - dl) * 2.0 ** (-(D + 1)); pi_minus = dl * 2.0 ** (-(D + 1))
    else:
        pi_plus = dl * 2.0 ** (-(D + 1)); pi_minus = (1 - dl) * 2.0 ** (-(D + 1))
    pmax = max(pi_plus, pi_minus)
    I = (1 - 2 * dl) ** 2 + 2 * dl * (1 - dl) * (D + 1) + 2 * w * dl
    m0 = (1 - 2 * dl) ** 2
    z = Z1(D, w)
    best = float('inf'); best_mix = float('inf')
    for lam in lam_grid():
        Lam = (1 << D) * (math.log1p(lam * pi_plus) + math.log1p(lam * pi_minus)) * LOG2E
        # exact single-root cost of {x0} in the cheapest gate: root + size(1) + norm(log Z1) - log theta(=0) + child(1)
        Cx0 = math.log2(1 / (lam * pmax)) + 1 + math.log2(z) + 1
        t = lam * pmax
        if t < 1:
            lb = m0 * Cx0 + Lam              # every other set costs >= 0
        else:
            # proof: every set costs >= -|A| log(1+t); sum_A p(A)|A| = I
            lb = Lam - I * math.log2(1 + t)
            lb = max(lb, Lam + m0 * Cx0 - (I - m0) * math.log2(1 + t))
        best = min(best, lb)
        best_mix = min(best_mix, Lam + Cx0)   # mixture bracket for {x0} (log 1/w_j >= 0 only adds)
    return best, best_mix, m0 * (D / 2 + 2), I


def witness_sum_x0(D, w):
    dl = 2.0 ** (-w)
    pis = (1 - dl) * 2.0 ** (-(D + 1)), dl * 2.0 ** (-(D + 1))
    Lam1 = (1 << D) * (math.log1p(pis[0]) + math.log1p(pis[1])) * LOG2E
    sum_pi = (1 << D) * (pis[0] + pis[1])
    Q = 2.0 ** (-Lam1) * sum_pi * 0.5 * (1.0 / Z1(D, w)) * 0.5
    return -math.log2(Q)


if __name__ == '__main__':
    print('(1) exact spectra of F_{D,w} (truth tables):')
    for D, w, n, ok, I in exact_spectrum_check():
        print(f'    D={D} w={w} n={n}: only phi-set {{x0}}, v=1, I formula exact: {ok}   I={I:.4f}')
    print('(2)-(3),(5) lower bounds over lambda in [2^-40, 2^80] (step 2^(1/8)):')
    worst_ratio = float('inf')
    for D in [4, 5, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128]:
        w = max(2, math.ceil(math.log2(D)))
        b, bm, target, I = lower_bound_scan(D, w)
        bc, bmc, _, _ = lower_bound_scan(D, w, complemented=True)
        worst_ratio = min(worst_ratio, b / target, bc / target, bm * (1 - 2 * 2.0 ** -w) ** 2 / target)
        print(f'    D={D:4d} w={w}: min_lam LB={b:9.3f}  compl={bc:9.3f}  mix-bracket(x m0)={bm*(1-2*2.0**-w)**2:9.3f}'
              f'  target (1-2d)^2(D/2+2)={target:8.3f}  I={I:.4f}  LB/I={b/I:7.2f}')
    print('    min over rows of LB/target =', round(worst_ratio, 4), '(must be >= 1)')
    print('(4) witness-sum cost of {x0}:')
    print('    ', [(D, round(witness_sum_x0(D, max(2, math.ceil(math.log2(D)))), 4)) for D in [1, 2, 4, 8, 16, 64, 256, 960]],
          ' sup bound 7.21; 2 zeta(6/5) =', 2 * 5.591582441177751)
