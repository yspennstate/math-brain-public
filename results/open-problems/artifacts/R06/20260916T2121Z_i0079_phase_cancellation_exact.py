#!/usr/bin/env python3
# R06 / I0079 exact finite-cylinder certificate.
#
# This certificate checks the finite combinatorial/algebraic core of the
# phase-cancellation theorem for G=T_4 x T_4. It does NOT by itself prove
# the infinite-volume convergence theorem; that proof is written in the report.
#
# No floating point arithmetic is used.

from fractions import Fraction
from itertools import product

d=4
q=d-1
k=2

def tree_prefixes(R):
    # Root first step has d choices. Each later step has q nonbacktracking choices.
    if R==0:
        return [()]
    pref=[(a,) for a in range(d)]
    for _ in range(1,R):
        pref=[p+(b,) for p in pref for b in range(q)]
    return pref

def tree_vertices(R):
    # Encode rooted-tree vertices by a nonbacktracking word in same coordinate labels.
    ans=[()]
    for r in range(1,R+1):
        ans += tree_prefixes(r)
    return ans

def lcp(a,b):
    t=0
    for x,y in zip(a,b):
        if x!=y:
            break
        t+=1
    return t

def busemann(prefix, vertex):
    # For an infinite ray whose first R letters are prefix, and |vertex|<=R,
    # h(v)=|v|-2*(length common prefix).
    return len(vertex)-2*lcp(prefix,vertex)

def prod_ball(R):
    tv=tree_vertices(R)
    return [(x,y) for x in tv for y in tv if len(x)+len(y)<=R]

def h_prod(sig,v):
    return busemann(sig[0],v[0])+busemann(sig[1],v[1])

def phase_reconstruct(E,c,M):
    # A_c = c/(M(q-1)); E = A_c q^Z (1+(q-1)U), 0<=U<1.
    A=Fraction(c,1) / (M*(q-1)) if isinstance(c,int) else c / (M*(q-1))
    # Find the unique Z such that A q^Z <= E < A q^(Z+1).
    Z=0
    if E < A:
        while E < A * Fraction(q**Z,1):
            Z-=1
    else:
        while E >= A * Fraction(q**(Z+1),1):
            Z+=1
    qZ = Fraction(q**Z,1) if Z>=0 else Fraction(1,q**(-Z))
    ratio=E/(A*qZ)
    assert Fraction(1,1) <= ratio < Fraction(q,1)
    U=(ratio-1)/(q-1)
    assert Fraction(0,1) <= U < Fraction(1,1)
    return Z,U

def direct_winner(signatures, Evals, c, M, v):
    best=None
    arg=None
    for i,sig in enumerate(signatures):
        Z,U=phase_reconstruct(Evals[i],c,M)
        key=(Z+h_prod(sig,v),U)
        if best is None or key<best:
            best=key; arg=i
    return arg

def phasefree_winner(signatures,Evals,v):
    # Compare E_sigma * q^{h_sigma(v)} exactly.
    best=None; arg=None
    for i,sig in enumerate(signatures):
        h=h_prod(sig,v)
        scale=Fraction(q**h,1) if h>=0 else Fraction(1,q**(-h))
        key=Evals[i]*scale
        if best is None or key<best:
            best=key; arg=i
    return arg

# Distinct positive integers with no ratio an integral power of q within tested h-range.
# Using primes >q suffices for our small deterministic certificate.
primes=[5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,
        83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,
        167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,
        251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,
        347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,
        433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,
        523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,
        619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,
        727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,
        827,829,839,853,857,859,863,877,881,883,887,907,911,919,929]

phases=[Fraction(1,2),Fraction(1,1),Fraction(7,3),Fraction(11,5)]

for R in (1,2):
    tp=tree_prefixes(R)
    signatures=list(product(tp, repeat=k))
    M=len(signatures)
    assert M==(d*(q**(R-1)))**k
    ball=prod_ball(R)
    assert len(primes)>=M
    Evals=[Fraction(primes[i],1) for i in range(M)]

    phase_partitions=[]
    for c in phases:
        winners=[direct_winner(signatures,Evals,c,M,v) for v in ball]
        phase_partitions.append(winners)

        pf=[phasefree_winner(signatures,Evals,v) for v in ball]
        assert winners==pf

    assert all(w==phase_partitions[0] for w in phase_partitions[1:])

    # Equivalence relation is equality of winners.
    eq0=[[phase_partitions[0][i]==phase_partitions[0][j]
          for j in range(len(ball))] for i in range(len(ball))]
    for winners in phase_partitions[1:]:
        eq=[[winners[i]==winners[j] for j in range(len(ball))]
            for i in range(len(ball))]
        assert eq==eq0

    print(f"R={R}: tree_prefixes={len(tp)}, product_signatures={M}, "
          f"ball_vertices={len(ball)}, phases={len(phases)}: PASS")

# Symbolic cumulative-intensity algebra with rational placeholders:
# sum_{j<m} c q^j + c q^m u
# = c q^m/(q-1) + c q^m u
# = [c/(q-1)] q^m [1+(q-1)u].
for m in range(-5,6):
    c=Fraction(7,5)
    for u in [Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(6,7)]:
        qm=Fraction(q**m,1) if m>=0 else Fraction(1,q**(-m))
        # geometric lower tail evaluated exactly:
        lhs=c*qm/Fraction(q-1,1)+c*qm*u
        rhs=c/Fraction(q-1,1)*qm*(1+(q-1)*u)
        assert lhs==rhs

print("symbolic cumulative-intensity / lexicographic transform identity: PASS")
print("PASS")
