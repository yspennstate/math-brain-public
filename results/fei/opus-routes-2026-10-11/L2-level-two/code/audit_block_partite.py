"""Second path for Corollary K (NOTES section 5e), sharing no code with block_partite.py.

Members of the class are built differently here: P = sum_r prod_k L_{r,k}(x_{X_k}) + c, a sum of products of affine forms,
one form per block (expanding gives monomials with at most one variable per block). Each case is admitted only after a
fiber test: for every block and every assignment of the other blocks, the fiber's Walsh vector (explicit Hadamard
matrix of the block) must be one-hot with entry +-1. Influences are read off the truth table, Inf_j = P(f(x) != f(x^j)),
not off the spectrum; the spectrum comes from an explicit Hadamard matrix. Checked:
    H(S_{X_k}) <= 2 (I - I_{X_k}) for every block,  H(S) <= sum_k H(S_{X_k}) <= 2 (K - 1) I,
and, as a control on the fiber test and on the inequalities, the same computation on polynomials that break the block
condition (one monomial with two variables of one block added).
Usage: python -B audit_block_partite.py
"""
import math
import numpy as np


def had(n):
    M = np.ones((1, 1))
    for _ in range(n):
        M = np.vstack([np.hstack([M, M]), np.hstack([M, -M])])
    return M


def H2(w):
    w = w[w > 1e-300]
    return float(-(w * np.log2(w)).sum())


def build(shape, terms, rng):
    n = sum(shape)
    offs = np.cumsum((0,) + tuple(shape))
    xs = np.arange(1 << n)
    bits = (xs[:, None] >> np.arange(n)[None, :]) & 1
    P = np.full(1 << n, int(rng.integers(2)), dtype=np.int64)
    for _ in range(terms):
        prod = np.ones(1 << n, dtype=np.int64)
        for k, s in enumerate(shape):
            a = rng.integers(0, 2, s)
            c = int(rng.integers(2))
            prod &= (bits[:, offs[k]:offs[k] + s] @ a + c) & 1
        P ^= prod
    return P, bits


def fibers_ok(F, shape):
    n = sum(shape)
    offs = np.cumsum((0,) + tuple(shape))
    xs = np.arange(1 << n)
    for k, s in enumerate(shape):
        blockmask = sum(1 << v for v in range(offs[k], offs[k] + s))
        Hb = had(s)
        rest = np.unique(xs & ~blockmask)
        inner = np.array([sum(((u >> t) & 1) << (offs[k] + t) for t in range(s)) for u in range(1 << s)])
        for r in rest:
            w = Hb @ F[r | inner] / (1 << s)
            nz = np.abs(w) > 1e-9
            if nz.sum() != 1 or abs(abs(w[nz][0]) - 1) > 1e-9:
                return False
    return True


def measure(F, shape):
    n = sum(shape)
    offs = np.cumsum((0,) + tuple(shape))
    xs = np.arange(1 << n)
    p = (had(n) @ F / (1 << n)) ** 2
    inf = np.array([np.mean(F != F[xs ^ (1 << j)]) for j in range(n)])
    I = float(inf.sum())
    Hs = H2(p)
    Hk, Ik = [], []
    for k, s in enumerate(shape):
        mask = sum(1 << v for v in range(offs[k], offs[k] + s))
        marg = np.zeros(1 << n)
        np.add.at(marg, xs & mask, p)
        Hk.append(H2(marg))
        Ik.append(float(inf[offs[k]:offs[k] + s].sum()))
    Ispec = float(sum(bin(S).count("1") * p[S] for S in range(1 << n)))
    return Hs, I, Hk, Ik, abs(I - Ispec)


def run(shape, cases, rng, broken=False):
    K = len(shape)
    n = sum(shape)
    offs = np.cumsum((0,) + tuple(shape))
    stat = dict(cases=0, rejected=0, viol=0, maxratio=0.0, minslack=math.inf, maxIdiff=0.0)
    for _ in range(cases):
        P, bits = build(shape, int(rng.integers(1, 2 * n)), rng)
        if broken:
            k = int(rng.integers(K))
            while shape[k] < 2:
                k = int(rng.integers(K))
            i, j = rng.choice(shape[k], 2, replace=False)
            P = P ^ (bits[:, offs[k] + i] & bits[:, offs[k] + j])
        F = (1 - 2 * P).astype(float)
        if not fibers_ok(F, shape):
            stat["rejected"] += 1
            if not broken:
                stat["viol"] += 1          # a member built as a sum of products must pass the fiber test
            else:                          # control: do the inequalities fail off the class?
                Hs, I, Hk, Ik, dI = measure(F, shape)
                off = any(h > 2 * (I - i) + 1e-9 for h, i in zip(Hk, Ik))
                stat["off_class_block_fail"] = stat.get("off_class_block_fail", 0) + int(off)
            continue
        Hs, I, Hk, Ik, dI = measure(F, shape)
        stat["cases"] += 1
        stat["maxIdiff"] = max(stat["maxIdiff"], dI)
        bad = Hs > sum(Hk) + 1e-9 or sum(Hk) > 2 * (K - 1) * I + 1e-9
        bad = bad or any(h > 2 * (I - i) + 1e-9 for h, i in zip(Hk, Ik))
        stat["viol"] += int(bad)
        if I > 1e-12:
            stat["maxratio"] = max(stat["maxratio"], Hs / I)
        for h, i in zip(Hk, Ik):
            stat["minslack"] = min(stat["minslack"], 2 * (I - i) - h)
    return stat


def main():
    rng = np.random.default_rng(1012)
    print("members (sum of products of affine forms, fiber test must pass)")
    for shape, cases in [((2, 2), 300), ((3, 3), 200), ((4, 3), 100), ((2, 2, 2), 300), ((3, 2, 2), 200),
                         ((3, 3, 2), 100), ((2, 2, 2, 2), 120), ((3, 3, 3), 40)]:
        st = run(shape, cases, rng)
        print(f"  {str(shape):14s} admitted={st['cases']:4d} rejected={st['rejected']} violations={st['viol']}  "
              f"max H/I={st['maxratio']:.6f} (bound {2 * (len(shape) - 1)})  min block slack={st['minslack']:.2e}  "
              f"max|I_table - I_spectrum|={st['maxIdiff']:.1e}", flush=True)
    print("control (one monomial with two variables of one block added): fiber test should reject")
    for shape, cases in [((2, 2, 2), 200), ((3, 3), 200)]:
        st = run(shape, cases, rng, broken=True)
        print(f"  {str(shape):14s} rejected={st['rejected']} of {cases}; admitted anyway={st['cases']} (expected 0); "
              f"block inequality H(S_Xk) <= 2(I - I_Xk) fails on {st.get('off_class_block_fail', 0)} of the rejected",
              flush=True)
    print("done")


if __name__ == "__main__":
    main()
