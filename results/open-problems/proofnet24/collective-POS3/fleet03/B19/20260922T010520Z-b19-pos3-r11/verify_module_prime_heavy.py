#!/usr/bin/env python3
"""Exact certificate for a width-three POS3 route counterexample.

Standard library only.  This does NOT refute POS3.  It refutes the stronger
route: connected + module-prime + no extremal balanced pair should force a
cross-chain insertion distribution with every slice <= e(P)/3.
"""
from itertools import combinations
from fractions import Fraction
import hashlib

N = 9
RELATIONS = [
    (0,2),(0,3),(0,4),
    (1,4),(1,5),
    (2,5),
    (3,6),(3,7),
    (4,7),(4,8),
    (5,8),(6,8),
]
CHAINS = ((0,3,6),(1,4,7),(2,5,8))
DUAL = {0:8, 8:0, 1:7, 7:1, 2:6, 6:2, 3:5, 5:3, 4:4}

def transitive_closure(n, rels):
    lt = [[False]*n for _ in range(n)]
    for a,b in rels:
        if a == b:
            raise AssertionError("loop")
        lt[a][b] = True
    for k in range(n):
        for i in range(n):
            if lt[i][k]:
                for j in range(n):
                    if lt[k][j]:
                        lt[i][j] = True
    if any(lt[i][i] for i in range(n)):
        raise AssertionError("cycle")
    return lt

def pred_masks(lt):
    out = []
    n = len(lt)
    for v in range(n):
        m = 0
        for u in range(n):
            if lt[u][v]:
                m |= 1 << u
        out.append(m)
    return out

def ideal_dp(lt):
    n = len(lt)
    full = (1 << n) - 1
    preds = pred_masks(lt)
    A = [0]*(1 << n)
    valid = [False]*(1 << n)
    valid[0] = True
    A[0] = 1
    for mask in range(1 << n):
        ok = True
        for v in range(n):
            if (mask >> v) & 1 and (preds[v] & mask) != preds[v]:
                ok = False
                break
        valid[mask] = ok
        if not ok or mask == 0:
            continue
        total = 0
        for v in range(n):
            if (mask >> v) & 1:
                prev = mask ^ (1 << v)
                if valid[prev]:
                    total += A[prev]
        A[mask] = total

    B = [0]*(1 << n)
    B[full] = 1
    for mask in range(full-1, -1, -1):
        if not valid[mask]:
            continue
        total = 0
        for v in range(n):
            if not ((mask >> v) & 1):
                nxt = mask | (1 << v)
                if valid[nxt] and (preds[v] & mask) == preds[v]:
                    total += B[nxt]
        B[mask] = total
    return A, B, valid, preds

def extension_count(lt):
    A,_,_,_ = ideal_dp(lt)
    return A[-1]

def pair_count(lt, x, y):
    assert not lt[x][y] and not lt[y][x]
    rels = [(i,j) for i in range(N) for j in range(N) if lt[i][j]]
    rels.append((x,y))
    return extension_count(transitive_closure(N, rels))

def incomparable(lt, x, y):
    return x != y and not lt[x][y] and not lt[y][x]

def width_exact(lt):
    best = 0
    witness = ()
    for r in range(1, N+1):
        for S in combinations(range(N), r):
            if all(incomparable(lt,a,b) for a,b in combinations(S,2)):
                best, witness = r, S
    return best, witness

def incomparability_connected(lt):
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(N):
            if v not in seen and incomparable(lt,u,v):
                seen.add(v)
                stack.append(v)
    return len(seen) == N

def autonomous(lt, M):
    M = set(M)
    for z in range(N):
        if z in M:
            continue
        cats = []
        for m in M:
            if lt[z][m]:
                cats.append(-1)
            elif lt[m][z]:
                cats.append(1)
            else:
                cats.append(0)
        if len(set(cats)) != 1:
            return False
    return True

def proper_autonomous_nontrivial(lt):
    ans = []
    for r in range(2, N):
        for M in combinations(range(N),r):
            if autonomous(lt,M):
                ans.append(M)
    return ans

def flux_vector(lt, x, chain):
    A,B,valid,preds = ideal_dp(lt)
    E = A[-1]
    W = [0]*(len(chain)+1)
    chainmask = sum(1 << y for y in chain)
    for mask in range(1 << N):
        if not valid[mask] or ((mask >> x) & 1):
            continue
        if (preds[x] & mask) != preds[x]:
            continue
        nxt = mask | (1 << x)
        if not valid[nxt]:
            continue
        t = (mask & chainmask).bit_count()
        W[t] += A[mask]*B[nxt]
    assert sum(W) == E
    return W

def mins_maxs(lt):
    mins = [v for v in range(N) if not any(lt[u][v] for u in range(N))]
    maxs = [v for v in range(N) if not any(lt[v][u] for u in range(N))]
    return mins,maxs

def verify_dual(lt):
    for i in range(N):
        for j in range(N):
            if lt[i][j] != lt[DUAL[j]][DUAL[i]]:
                return False
    return True

lt = transitive_closure(N, RELATIONS)
E = extension_count(lt)
assert E == 349
w, anti = width_exact(lt)
assert w == 3
assert incomparability_connected(lt)
assert verify_dual(lt)

mods = proper_autonomous_nontrivial(lt)
assert mods == []

mins,maxs = mins_maxs(lt)
assert mins == [0,1]
assert maxs == [7,8]

pair_rows = []
balanced = []
endpoint_balances = []
for x,y in combinations(range(N),2):
    if incomparable(lt,x,y):
        num = pair_count(lt,x,y)
        bal = min(num,E-num)
        row = (x,y,num,bal)
        pair_rows.append(row)
        if E <= 3*num <= 2*E:
            balanced.append((x,y,num))
        if x in mins or x in maxs or y in mins or y in maxs:
            endpoint_balances.append((x,y,num,bal))

assert balanced == [(2,3,156),(5,6,156)]
assert max(r[3] for r in endpoint_balances) == 105
assert 3*105 < E

flux_rows = []
min_of_max = None
for a,chain_a in enumerate(CHAINS):
    for x in chain_a:
        for b,chain_b in enumerate(CHAINS):
            if a == b:
                continue
            if not any(incomparable(lt,x,y) for y in chain_b):
                continue
            W = flux_vector(lt,x,chain_b)
            M = max(W)
            flux_rows.append((x,b,W,M))
            min_of_max = M if min_of_max is None else min(min_of_max,M)
            assert 3*M > E
assert min_of_max == 142

print("POS3_B19_MODULE_PRIME_HEAVY_CERTIFICATE")
print("relations =", RELATIONS)
print("chains =", CHAINS)
print("self_dual =", True)
print("extensions =", E)
print("width =", w, "antichain_witness =", anti)
print("incomparability_connected =", True)
print("proper_nontrivial_autonomous_subsets =", mods)
print("minimal =", mins, "maximal =", maxs)
print("balanced_pairs (x,y,#x<y) =", balanced)
print("max_extremal_balance_numerator =", max(r[3] for r in endpoint_balances),
      "over", E, "=", Fraction(max(r[3] for r in endpoint_balances),E))
print("endpoint_rows =", endpoint_balances)
print("E_over_3 =", f"{E}/3")
print("minimum_relevant_max_flux =", min_of_max, "over", E, "=", Fraction(min_of_max,E))
print("flux_rows:")
for x,b,W,M in flux_rows:
    print(" ", (x,b), tuple(W), "max=", M)
print("CONCLUSION: connected + module-prime + no extremal balanced pair does not force a light (<=E/3) relevant insertion-slice vector.")
print("PARENT_POS3_STATUS: OPEN_NOT_PROVED")
print("POS3_B19_MODULE_PRIME_HEAVY_CERTIFICATE_PASS")
