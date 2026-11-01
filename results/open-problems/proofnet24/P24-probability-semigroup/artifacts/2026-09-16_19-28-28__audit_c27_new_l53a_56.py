from itertools import product
from math import comb

# Exact finite self-check for the P24 audit of C27 claim NEW-L53A.
# This checker verifies only finite/combinatorial algebra used in the audit:
# tree-cut binomial law on sample trees, the median threshold, ceiling identities,
# and the final cross-heat constant implication. It does not replace the written
# strong-Rayleigh/negative-association proof in the run report.

def ceil_div(a,b):
    return (a+b-1)//b

def cut_hist(k, edges):
    out = [0]*k
    for bits in product((0,1), repeat=k):
        z = sum(bits[u] != bits[v] for (u,v) in edges)
        out[z] += 1
    return out

def path_edges(k):
    return [(i,i+1) for i in range(k-1)]

def star_edges(k):
    return [(0,i) for i in range(1,k)]

def heap_tree_edges(k):
    return [((i-1)//2,i) for i in range(1,k)]

for k in range(2,9):
    target = [2*comb(k-1,j) for j in range(k)]
    for name, edges in [
        ("path", path_edges(k)),
        ("star", star_edges(k)),
        ("heap", heap_tree_edges(k)),
    ]:
        h = cut_hist(k, edges)
        assert h == target, (k,name,h,target)

for k in range(2,129):
    m = k-1
    z0 = ceil_div(m,2)
    s = ceil_div(m,4)
    # Fair Bin(m,1/2) has at least half its mass at or above ceil(m/2).
    tail_numer = sum(comb(m,j) for j in range(z0,m+1))
    assert 2*tail_numer >= 2**m

    # If Z >= ceil(m/2) and the directed red->blue count N satisfies 2N >= Z,
    # then N >= ceil(m/4).
    assert ceil_div(z0,2) == s

    # H <= m/(4e) and Lambda <= H/2 imply
    # e*Lambda/s <= m/(8s) <= 1/2.  The factor e cancels exactly.
    assert m <= 4*s

print("P24 AUDIT C27 NEW-L53A EXACT CHECK")
print("sample tree cut histograms: PASS for path/star/heap, k=2..8")
print("binomial median threshold: PASS for k=2..128")
print("ceil(ceil((k-1)/2)/2)=ceil((k-1)/4): PASS")
print("cross-heat implication m/(8 s_k) <= 1/2: PASS")
print("ALL_EXACT_CHECKS_PASS")
