#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from collections import Counter
import sympy as sp

checks = 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for r in range(1, len(items)):
        b = items[r]
        rest = items[1:r] + items[r+1:]
        for M in perfect_matchings(rest):
            yield ((a,b),) + M

def col_states(K,m):
    ans=[]
    for S in combinations(range(K),m):
        ss=set(S)
        ans.append(tuple(1 if i in ss else 0 for i in range(K)))
    return ans

def fixed_matching_distribution(state, M):
    # state is tuple of columns; every differing matched pair/column
    # is independently swapped with probability 1/2.
    active=[]
    for a,b in M:
        for l,col in enumerate(state):
            if col[a] != col[b]:
                active.append((a,b,l))
    out={}
    for bits in product((0,1), repeat=len(active)):
        cols=[list(c) for c in state]
        for z,(a,b,l) in zip(bits,active):
            if z:
                cols[l][a],cols[l][b]=cols[l][b],cols[l][a]
        ns=tuple(tuple(c) for c in cols)
        out[ns]=out.get(ns,Fraction(0))+Fraction(1,2**len(active))
    ck(sum(out.values(),Fraction(0))==1, "fixed matching distribution not normalized")
    return out

def transition(K, ms):
    matchings=list(perfect_matchings(range(K)))
    state_lists=[col_states(K,m) for m in ms]
    states=list(product(*state_lists))
    ix={s:i for i,s in enumerate(states)}
    N=len(states)
    P=[[Fraction(0) for _ in range(N)] for __ in range(N)]
    for i,s in enumerate(states):
        for M in matchings:
            for ns,p in fixed_matching_distribution(s,M).items():
                P[i][ix[ns]] += p/Fraction(len(matchings))
        ck(sum(P[i],Fraction(0))==1, "transition row not normalized")
    # exact symmetry (uniform stationary law)
    for i in range(N):
        for j in range(N):
            ck(P[i][j]==P[j][i], "transition matrix not symmetric")
    return states,P

def apply(P, f):
    return [sum((P[i][j]*f[j] for j in range(len(f))), Fraction(0))
            for i in range(len(f))]

# 1. Pairwise cross-column eigenfunction:
# F(x,y)=sum_i (x_i-m1/K)(y_i-m2/K)
# must have eigenvalue (K-2)/(2(K-1)).
for K in (2,4,6):
    lam=Fraction(K-2,2*(K-1))
    for m1 in range(1,K):
        for m2 in range(1,K):
            states,P=transition(K,(m1,m2))
            f=[]
            for x,y in states:
                val=sum((Fraction(x[i])-Fraction(m1,K))*
                        (Fraction(y[i])-Fraction(m2,K))
                        for i in range(K))
                f.append(val)
            Pf=apply(P,f)
            for a,b in zip(Pf,f):
                ck(a==lam*b, f"pair eigenfunction failed K={K}, m={m1},{m2}")

# 2. One-column walk is exactly the quotient of a uniform perfect
# matching with independently active transpositions. Conditional on
# b active transpositions, every b-matching must have equal probability.
for K in (2,4,6,8):
    matchings=list(perfect_matchings(range(K)))
    weights=Counter()
    for M in matchings:
        E=len(M)
        for bits in product((0,1), repeat=E):
            F=tuple(sorted(tuple(sorted(M[r])) for r,z in enumerate(bits) if z))
            weights[F]+=Fraction(1,len(matchings)*2**E)
    by_b={}
    for F,p in weights.items():
        by_b.setdefault(len(F),set()).add(p)
    for b,vals in by_b.items():
        ck(len(vals)==1, f"active b-matchings not equiprobable K={K}, b={b}")
        total=sum(p for F,p in weights.items() if len(F)==b)
        # B ~ Bin(K/2,1/2)
        expected=Fraction(sp.binomial(K//2,b),2**(K//2))
        ck(total==expected, f"wrong Binomial active-count law K={K}, b={b}")

# 3. Exact small-case spectra: multi-column shared-matching chain has
# no extra second eigenvalue in these complete enumerations.
def exact_spectrum(P):
    M=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in P])
    return M.eigenvals()

small_cases=[
    (4,(1,)), (4,(2,)), (4,(3,)),
    (4,(1,1)), (4,(1,2)), (4,(2,2)),
    (6,(1,)), (6,(2,)), (6,(3,))
]
specs={}
for K,ms in small_cases:
    states,P=transition(K,ms)
    eig=exact_spectrum(P)
    vals=sorted(eig.keys(), key=lambda z: float(z), reverse=True)
    ck(vals[0]==1 and eig[vals[0]]==1, f"stationary eigenvalue wrong {K},{ms}")
    ck(all(v>=0 for v in vals), f"negative eigenvalue {K},{ms}")
    specs[(K,ms)]=(vals,eig)

# K=4 two-column cases: lambda_2 equals max of one-column lambda_2.
for ms in ((1,1),(1,2),(2,2)):
    vals,eig=specs[(4,ms)]
    l2=vals[1]
    singles=[]
    for m in ms:
        v,_=specs[(4,(m,))]
        singles.append(v[1])
    ck(l2==max(singles), f"spectral tensor equality failed K=4, ms={ms}")

# Explicit rational spectra used in the report.
v,e=specs[(4,(2,))]
ck(v==[sp.Rational(1),sp.Rational(1,2),sp.Rational(1,3)], "K4 m2 spectrum")
ck([e[x] for x in v]==[1,2,3], "K4 m2 multiplicities")
v,e=specs[(4,(2,2))]
ck(v==[sp.Rational(1),sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,4),sp.Rational(0)], "K4 m2m2 spectrum")
ck([e[x] for x in v]==[1,5,15,2,13], "K4 m2m2 multiplicities")
v,e=specs[(6,(3,))]
ck(v==[sp.Rational(1),sp.Rational(2,5),sp.Rational(1,3),sp.Rational(1,5)], "K6 m3 spectrum")
ck([e[x] for x in v]==[1,5,9,5], "K6 m3 multiplicities")

print("CHECKS", checks)
print("PAIR_EIGENVALUE_FORMULA lambda_K=(K-2)/(2(K-1)) verified K=2,4,6 all nontrivial column sums")
print("INVOLUTION_GENERATOR counting verified K=2,4,6,8")
print("SPECTRUM K4_m2", specs[(4,(2,))])
print("SPECTRUM K4_m2_m2", specs[(4,(2,2))])
print("SPECTRUM K6_m3", specs[(6,(3,))])
print("ALL_EXACT_P0251_SHARED_MATCHING_SPECTRAL_CHECKS_PASS")
