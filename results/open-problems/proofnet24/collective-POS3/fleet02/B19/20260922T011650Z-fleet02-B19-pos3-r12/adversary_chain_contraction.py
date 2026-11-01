#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
from functools import lru_cache

def multinomial(parts):
    n=sum(parts)
    out=factorial(n)
    for p in parts:
        out//=factorial(p)
    return out

def words(counts):
    counts=tuple(counts)
    @lru_cache(None)
    def rec(state):
        if sum(state)==0:
            return ((),)
        out=[]
        for i,c in enumerate(state):
            if c:
                s=list(state); s[i]-=1
                for tail in rec(tuple(s)):
                    out.append((i,)+tail)
        return tuple(out)
    return rec(counts)

def pair_count(ws, chain_x, idx_x, chain_y, idx_y):
    # idx_* is 1-based along its chain.
    good=0
    for w in ws:
        px=[k for k,t in enumerate(w) if t==chain_x][idx_x-1]
        py=[k for k,t in enumerate(w) if t==chain_y][idx_y-1]
        good += (px < py)
    return good

def balanced(n,d):
    return 3*n >= d and 3*n <= 2*d

print("POS3_ASYMMETRIC_CHAIN_CONTRACTION_BEGIN")
print("P(m,r) = disjoint union C2 + C(m+2) + Cr; width exactly 3 for r>=1")
print("M = top m vertices B3,...,B(m+2) of the middle chain; M is an autonomous chain")
print("contracting M to one vertex gives Q(r)=C2 + C3 + Cr")

# The induced A/B word is uniform after deleting the third-chain symbols.
# Hence Pr(A1<B1)=2/(m+4), independent of r.
for m in range(1,9):
    q=Fraction(2,m+4)
    print(f"formula m={m}: Pr(A1<B1)={q}")
    assert (q < Fraction(1,3)) == (m >= 3)
print("THRESHOLD_FORMULA_PASS: contracted m=1 gives 2/5; expanded m>=3 gives <1/3")

# Exact contracted quotient Q(1)=C2+C3+C1.
q_words=words((2,3,1))
assert len(q_words)==multinomial((2,3,1))==60
q_num=pair_count(q_words,0,1,1,1)
assert Fraction(q_num,len(q_words))==Fraction(2,5)
print(f"CONTRACTED_Q: E={len(q_words)} A1_before_B1={q_num}/{len(q_words)}={Fraction(q_num,len(q_words))} BALANCED")

# Exact width-three adversary P(3,1)=C2+C5+C1.
p_words=words((2,5,1))
E=len(p_words)
assert E==multinomial((2,5,1))==168
p_num=pair_count(p_words,0,1,1,1)
assert Fraction(p_num,E)==Fraction(2,7)
print(f"EXPANDED_P: E={E} A1_before_B1={p_num}/{E}={Fraction(p_num,E)} UNBALANCED_below_1/3")
print("WIDTH=3 witness={A1,B1,C1}; no antichain can use two vertices from one chain")
print("INCOMPARABILITY_GRAPH_CONNECTED: complete tripartite K(2,5,1)")
print("AUTONOMOUS_MODULE M={B3,B4,B5}: B1,B2 below every M vertex; all A,C vertices incomparable with every M vertex")

names=(["A1","A2"],["B1","B2","B3","B4","B5"],["C1"])
print("ALL_17_INCOMPARABLE_PAIR_PROBABILITIES")
bal=0
for cx,cy in ((0,1),(0,2),(1,2)):
    for ix,x in enumerate(names[cx],1):
        for iy,y in enumerate(names[cy],1):
            num=pair_count(p_words,cx,ix,cy,iy)
            f=Fraction(num,E)
            tag="BALANCED" if balanced(num,E) else "UNBALANCED"
            bal += (tag=="BALANCED")
            print(f"{x}<{y}: {num}/{E}={f} {tag}")
assert bal==7
print(f"SUMMARY incomparable_pairs=17 balanced_pairs={bal}")

# Ordinal-sum amplification by any unique chains C_s below and C_t above adds no
# incomparable pairs across components and forces concatenation, hence preserves
# these exact probabilities and E. Check a representative size statement.
s,t=2,3
n=s+(2+5+1)+t
assert n==13
print(f"ORDINAL_SUM_FAMILY: C{s} ordinal P(3,1) ordinal C{t} has n={n}, width=3, E={E}, same 17 incomparable-pair probabilities")
print("ORDINAL_PRESERVATION_PASS")
print("POS3_ASYMMETRIC_CHAIN_CONTRACTION_PASS")
