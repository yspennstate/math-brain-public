#!/usr/bin/env python3
"""
Exact self-check for R20's loop-free d_D=2 subcubic-core construction.

Checks:
1. exact chain completion laws for boundary pushes alpha,beta in {2,3};
2. exact branch-vs-chain separation for d_D=2 with branch pushes in {2,3};
3. all 3^5 local pairings of the K5 quotient exceptional case, using the
   explicit one-defect construction from the written proof;
4. confirms that the all-branch-push-3 ansatz cannot solve a K5 quotient,
   since it would require 5 distinct ports from {0,1,2,3}.

All arithmetic is integer arithmetic.
"""
from itertools import product

COLORS = range(4)

def chain_sigmas(alpha, beta, word):
    k = len(word)
    w = [alpha] + list(word) + [beta]
    return [2 * (1 + w[i]) + w[i-1] + w[i+1] for i in range(1, k+1)]

def chain_proper(alpha, beta, word):
    s = chain_sigmas(alpha, beta, word)
    return all(s[i] != s[i+1] for i in range(len(s)-1)
               )

def complete_chain(alpha, beta, a, b, k):
    assert k >= 1
    if k == 1:
        if a != b:
            return None
        return [a]
    if k == 2:
        if a - b == beta - alpha:
            return None
        return [a,b]
    if k == 3:
        for x in COLORS:
            w = [a,x,b]
            if chain_proper(alpha,beta,w):
                return w
        raise AssertionError("k=3 completion missing")
    if k == 4:
        for x in COLORS:
            w = [a,0,x,b]
            if chain_proper(alpha,beta,w):
                return w
        raise AssertionError("k=4 completion missing")

    w = [None]*(k+2)
    w[0], w[1], w[k], w[k+1] = alpha, a, b, beta
    w[2] = 0
    for j in range(3, k-1):
        for x in COLORS:
            if w[j-3] + w[j-2] != w[j-1] + x:
                w[j] = x
                break
        assert w[j] is not None
    for x in COLORS:
        w[k-1] = x
        ok = True
        for i in range(k-3, k):
            if w[i-1] + w[i] == w[i+1] + w[i+2]:
                ok = False
                break
        if ok:
            word = w[1:k+1]
            assert chain_proper(alpha,beta,word)
            return word
    raise AssertionError("final completion missing")

chain_cases = 0
for alpha,beta in product((2,3), repeat=2):
    for a,b in product(COLORS, repeat=2):
        got = complete_chain(alpha,beta,a,b,1)
        assert (got is not None) == (a == b)
        chain_cases += 1

        got = complete_chain(alpha,beta,a,b,2)
        expected = (a-b != beta-alpha)
        assert (got is not None) == expected
        if got is not None:
            assert chain_proper(alpha,beta,got)
        chain_cases += 1

        for k in range(3,101):
            got = complete_chain(alpha,beta,a,b,k)
            assert got is not None
            assert got[0] == a and got[-1] == b
            assert chain_proper(alpha,beta,got)
            chain_cases += 1

gap_cases = 0
min_gap = None
for r,r1,r2,p,q in product((2,3),(2,3),(2,3),COLORS,COLORS):
    sb = 3*(1+r) + r1+r2+p
    sx = 2*(1+p) + r+q
    gap = sb-sx
    assert gap > 0
    min_gap = gap if min_gap is None else min(min_gap,gap)
    gap_cases += 1
for r,r1,r2,p,s in product((2,3),(2,3),(2,3),COLORS,(2,3)):
    sb = 3*(1+r) + r1+r2+p
    sx = 2*(1+p) + r+s
    gap = sb-sx
    assert gap > 0
    min_gap = min(min_gap,gap)
    gap_cases += 1

V = tuple(range(5))
def partitions_of_four(items):
    items = tuple(items)
    a = items[0]
    out = []
    for b in items[1:]:
        first = tuple(sorted((a,b)))
        rest = tuple(x for x in items if x not in first)
        out.append((first,tuple(sorted(rest))))
    return out
PARTS = {q: partitions_of_four([r for r in V if r != q]) for q in V}

def pairing_data(cfg):
    groups = {}
    side = {}
    for q in V:
        groups[q] = PARTS[q][cfg[q]]
        for s,g in enumerate(groups[q]):
            for r in g:
                side[(q,r)] = s
    return groups,side

def explicit_ports(cfg):
    groups,side = pairing_data(cfg)
    A = 0
    S = list(groups[A][0])
    s0,s1 = S
    sh0 = (side[(s0,A)] == side[(s0,s1)])
    sh1 = (side[(s1,A)] == side[(s1,s0)])
    if sh0 and not sh1:
        low,high = s0,s1
    elif sh1 and not sh0:
        low,high = s1,s0
    else:
        low,high = sorted(S)
    p = {A:0, low:0, high:1}
    T = sorted(set(V)-{A,*S})
    p[T[0]],p[T[1]] = 2,3
    return p,side

def actual_graph(cfg):
    groups,side = pairing_data(cfg)
    edges = []
    for q in V:
        for r in range(q+1,5):
            edges.append((2*q+side[(q,r)], 2*r+side[(r,q)]))
    for q in V:
        edges.append((2*q,10+q))
        edges.append((10+q,2*q+1))
    return edges

k5_configs = 0
for cfg in product(range(3), repeat=5):
    p,side = explicit_ports(cfg)
    edges = actual_graph(cfg)
    adj = [[] for _ in range(15)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    rho = [None]*15
    for q in V:
        rho[2*q] = 2 if q == 0 else 3
        rho[2*q+1] = 3
        rho[10+q] = p[q]
    sigma = [
        len(adj[u])*(1+rho[u]) + sum(rho[v] for v in adj[u])
        for u in range(15)
    ]
    assert all(sigma[u] != sigma[v] for u,v in edges)
    assert max(rho) <= 3

    assert not any(
        all(ps[q] != ps[r] for q in V for r in range(q+1,5))
        for ps in product(COLORS, repeat=5)
    )
    k5_configs += 1

print(f"chain_constructive_cases={chain_cases}")
print("chain_lengths_checked=1..100")
print(f"branch_chain_gap_cases={gap_cases}")
print(f"minimum_branch_minus_chain_sigma_gap={min_gap}")
print(f"k5_local_pairing_configs_checked={k5_configs}")
print("k5_all3_ansatz_successes=0")
print("k5_one_defect_failures=0")
print("VERDICT=PASS")
print("STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6")
