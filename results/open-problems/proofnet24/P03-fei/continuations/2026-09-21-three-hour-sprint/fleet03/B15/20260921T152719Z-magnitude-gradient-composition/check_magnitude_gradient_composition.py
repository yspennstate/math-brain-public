"""Exploratory verifier for B15 magnitude-gradient composition and rare-tribes cancellation.

All theorem identities in the accompanying report are analytic. Numaro recursion
values here are floating-point exploratory checks; the truth-table identity is
accepted only after matching the preserved external SHA-256.
"""
from __future__ import annotations
import hashlib
import math
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2 and not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    table = np.tile(core, (1 << 9, 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << 9) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA and int(table.sum()) == 0
    return table

def fwht(a):
    a = np.asarray(a, dtype=np.int64).copy()
    h = 1
    while h < a.size:
        b = a.reshape(-1, 2*h)
        x = b[:, :h].copy()
        y = b[:, h:].copy()
        b[:, :h], b[:, h:] = x+y, x-y
        a = b.reshape(-1)
        h *= 2
    return a

def pairs(coeff, i):
    bit = 1 << i
    low = np.array([j for j in range(coeff.size) if not (j & bit)], dtype=np.int64)
    return np.abs(coeff[low]), np.abs(coeff[low | bit])

def base_stats(coeff, i):
    u, v = pairs(coeff, i)
    inf = float(np.sum(v*v))
    mask = (u > 0) & (v > 0)
    L = float(np.sum(v[mask]**2 * np.maximum(0.0, np.log2(u[mask]/v[mask]))))
    return inf, L, abs(float(coeff[1 << i]))

def M(coeff, i, q):
    u, v = pairs(coeff, i)
    mask = (u > 0) & (v > 0)
    return float(np.sum(v[mask]**2 * np.maximum(0.0, np.log2(u[mask]/(v[mask]*q)))))

def rare_tribes_ratio(m, w):
    eps = 2.0**(-w)
    q = 1.0-eps
    c = abs(2*q**m-1)
    a1 = 2*eps*q**(m-1)
    term0 = 4*eps**2*q**(2*m-2)*max(0.0, math.log2(c/a1))
    Q = 2**w-1
    term1 = 4*eps**2*q**(m-1)*(1-q**(m-1))*math.log2(Q)
    inf = 2*eps*q**(m-1)
    return (term0+term1)/inf

def main():
    table = reconstruct()
    W = fwht(table)
    coeff = W.astype(np.float64) / table.size
    C = base_stats(coeff, 0)
    A = base_stats(coeff, 9)
    assert abs(C[0]-57/256) < 1e-15 and abs(C[2]-57/256) < 1e-15
    assert abs(A[0]-1/256) < 1e-15 and abs(A[2]-1/256) < 1e-15
    print("truth_table_sha256", EXPECTED_SHA)
    print("base_C_L_over_Inf", C[1]/C[0])
    print("base_A_L_over_Inf", A[1]/A[0])

    alpha = {"C": C[0], "A": A[0]}
    idx = {"C": 0, "A": 9}
    baseell = {"C": C[1]/C[0], "A": A[1]/A[0]}
    dp = {(1,0): (baseell["C"], "C"), (0,1): (baseell["A"], "A")}
    print("depth 1 min", min(v[0] for v in dp.values()))
    cache = {}
    for depth in range(2, 16):
        nd = {}
        for (nc,na), (ell,path) in dp.items():
            q = alpha["C"]**nc * alpha["A"]**na
            for name in ("C","A"):
                keym=(nc,na,name)
                if keym not in cache:
                    cache[keym]=M(coeff, idx[name], q)
                inc = q * cache[keym] / alpha[name]  # q^2/p=q for this seed
                key=(nc+(name=="C"), na+(name=="A"))
                cand=(ell+inc, path+name)
                if key not in nd or cand[0] < nd[key][0]:
                    nd[key]=cand
        dp=nd
        best=min(dp.values(), key=lambda z:z[0])
        print("depth", depth, "min", best[0], "path", best[1])

    for a,w in [(1,12),(2,12),(3,12),(4,16),(6,18)]:
        m=2**a+1
        print("rare", "a",a,"m",m,"w",w,
              "L_over_Inf", rare_tribes_ratio(m,w),
              "D_selector_asymptotic", 2*(m-1)*a)

if __name__ == "__main__":
    main()
