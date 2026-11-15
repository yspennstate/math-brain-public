#!/usr/bin/env python3
"""Local, bounded referee checks. No network, workers, or external writes."""
import os
os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
import itertools
import math
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path
import re
import sympy as S

signal.alarm(240)
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
started = time.monotonic()

def automaton(children):
    odd = [c for c in children if c]
    return odd[0] if len(odd) == 1 else 0

def exact_map(law, x):
    ans = [F(0) for _ in x]
    for n, probability in law.items():
        for children in itertools.product(range(len(x)), repeat=n):
            weight = probability
            for child in children:
                weight *= x[child]
            ans[automaton(children)] += weight
    return ans

print("EXACT ORDERED-CONFIGURATION CHECKS")
laws = {
    "binary": {2:F(1)},
    "unary_binary": {1:F(2,5), 2:F(3,5)},
    "leaf_supercritical": {0:F(1,4), 2:F(3,4)},
    "critical": {0:F(1,2), 2:F(1,2)},
    "subcritical": {0:F(3,4), 2:F(1,4)},
    "mixed": {0:F(1,10), 1:F(1,5), 3:F(3,10), 5:F(2,5)},
}
xs = [[F(0),F(1,3),F(2,3)], [F(1,2),F(1,6),F(1,3)],
      [F(3,4),F(1,8),F(1,8)], [F(1),F(0),F(0)],
      [F(1,3),F(1,6),F(1,4),F(1,4)]]
count = 0
for name, law in laws.items():
    for x in xs:
        s = x[0]
        derivative = sum(prob*n*s**(n-1) for n,prob in law.items() if n)
        predicted = [1-(1-s)*derivative] + [q*derivative for q in x[1:]]
        assert exact_map(law,x) == predicted, (name,x)
        count += 1
print(f"{count} exact maps PASS (k=2,3; s=0,1 included)")

print("\nEXACT PIVOTALITY AND MERGING")
checked = 0
for n in range(9):
    for children in itertools.product(range(2), repeat=n):
        parent = automaton(children)
        piv = []
        for j, child in enumerate(children):
            switched = list(children)
            switched[j] = 1-child
            piv.append(automaton(switched) != parent)
        odd = sum(children)
        expected = [odd == 1 or odd == 0 or (odd == 2 and c == 1) for c in children]
        assert piv == expected
        checked += 1
    for children in itertools.product(range(3), repeat=n):
        merge = lambda c: int(c != 0)
        assert merge(automaton(children)) == automaton([merge(c) for c in children])
print(f"{checked} binary configurations through degree 8 PASS; 9841 three-state merges PASS")

def derivative_exact(law, s, order):
    return sum(prob*math.prod(range(n-order+1,n+1))*s**(n-order)
               for n,prob in law.items() if n >= order)

for name, s in [("binary",F(1,2)), ("unary_binary",F(1,2)),
                ("leaf_supercritical",F(2,3))]:
    law = laws[name]
    p = 1-s
    mass = [p,s]
    matrix = [[F(0),F(0)],[F(0),F(0)]]
    for n,prob in law.items():
        for children in itertools.product(range(2),repeat=n):
            weight = prob*math.prod(p if c else s for c in children)
            parent = automaton(children)
            row = 0 if parent else 1
            for j,c in enumerate(children):
                switched = list(children)
                switched[j] = 1-c
                if automaton(switched) != parent:
                    matrix[row][0 if c else 1] += weight/mass[row]
    g2 = derivative_exact(law,s,2)
    expected = [[F(1),s*g2],[p*p*g2/s,F(1)]]
    assert matrix == expected
    assert exact_map(law,[s,p/3,2*p/3]) == [s,p/3,2*p/3]
    print(f"{name}: s={s}, M={[[str(v) for v in row] for row in matrix]}, rho={1+p*g2} PASS")

print("\nSYMBOLIC CHECKS")
x,y,z,r,lam,u,v = S.symbols("x y z r lambda u v", real=True)
rz = [2*x*z, 2*y*z, 1-2*(x+y)+2*(x+y)**2]
target = [2*x*z,2*y*z,z*z+(x+y)**2]
assert all(S.expand((a-b).subs(z,1-x-y)) == 0 for a,b in zip(rz,target))
assert all(S.simplify((a-b).subs({z:S.Rational(1,2),y:S.Rational(1,2)-x})) == 0
           for a,b in zip(target,[x,y,z]))
assert S.simplify((r+2*(1-r)*u-1).subs(u,S.Rational(1,2))) == 0
positive_lam = S.symbols("L", positive=True)
star = 1-S.log(positive_lam)/positive_lam
assert S.simplify(positive_lam*S.exp(positive_lam*(star-1))) == 1
assert S.simplify((1-star)*positive_lam**2*S.exp(positive_lam*(star-1))) == S.log(positive_lam)
symbolic_M = S.Matrix([[1,u*v],[(1-u)**2*v/u,1]])
assert S.factor(symbolic_M.charpoly().as_expr()) == S.factor((symbolic_M.charpoly().gen-1)**2-(1-u)**2*v*v)
print("RZ equation (21) at (a,b,c)=(0,0,1); fixed segment; r-mixture; Poisson root and rho; characteristic polynomial: PASS")
print("Binary fixed equations: x(1-2(x+y))=y(1-2(x+y))=0; locus origin or x+y=1/2")

def bisect_root(g1):
    lo,hi = 0.0, 1.0-1e-12
    assert g1(lo) < 1 < g1(hi)
    for _ in range(100):
        mid = (lo+hi)/2
        if g1(mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

print("\nNUMERICAL SERIES CHECKS (deterministic summation, no simulation)")
numeric_laws = [
    ("leaf .25/unary .25/ternary .50",lambda n:{0:.25,1:.25,3:.5}.get(n,0.),
     lambda s:.25+1.5*s*s,lambda s:3*s,20),
    ("Poisson(2)",lambda n:math.exp(-2)*2**n/math.factorial(n),
     lambda s:2*math.exp(2*(s-1)),lambda s:4*math.exp(2*(s-1)),100),
    ("1/[n(n-1)] infinite mean",lambda n:1/(n*(n-1)) if n>=2 else 0.,
     lambda s:-math.log1p(-s),lambda s:1/(1-s),2000),
    (".25 delta0 + .75 heavy tail",lambda n:.25 if n==0 else (.75/(n*(n-1)) if n>=2 else 0.),
     lambda s:-.75*math.log1p(-s),lambda s:.75/(1-s),2000),
]
for name,chi,g1,g2,cutoff in numeric_laws:
    s = bisect_root(g1)
    p = 1-s
    maxerr = 0.
    for a in [.1,.5,s,.9]:
        # Sum probabilities of each possible unique odd-child position.
        b1,b2 = (1-a)/3,2*(1-a)/3
        odds = [math.fsum(chi(n)*n*q*a**(n-1) for n in range(1,cutoff+1))
                for q in (b1,b2)]
        actual = [1-sum(odds),*odds]
        predicted = [1-(1-a)*g1(a),b1*g1(a),b2*g1(a)]
        maxerr = max(maxerr,max(abs(c-d) for c,d in zip(actual,predicted)))
    assert maxerr < 1e-12
    # Independent binomial-count summation of all pivotal-child counts.
    m_ba = math.fsum(chi(n)*n*p*s**(n-1)*(n-1)/p for n in range(1,cutoff+1))
    m_ab = math.fsum(chi(n)*n*(n-1)*p*p*s**(n-2)/s for n in range(2,cutoff+1))
    m_aa = math.fsum(chi(n)*s**n*n/s for n in range(1,cutoff+1))
    m_bb = math.fsum(chi(n)*n*p*s**(n-1)/p for n in range(1,cutoff+1))
    assert max(abs(m_ba-s*g2(s)),abs(m_ab-p*p*g2(s)/s),abs(m_aa-1),abs(m_bb-1)) < 1e-12
    print(f"{name}: s*={s:.12f}, rho={1+p*g2(s):.12f}, max map error={maxerr:.3g}, pivot matrix PASS")

# Infinite logarithmic moment test: P(N=2^(2^j))=1/[j(j+1)].
# Only j<=4 is needed at the tested s: all omitted degrees are >=2^32.
degrees = [(2**(2**j),1/(j*(j+1))) for j in range(1,5)]
def sparse_g1(s):
    if s == 0:
        return 0.
    return math.fsum(w*n*s**(n-1) for n,w in degrees)
lo,hi = 0.,.99
for _ in range(100):
    mid = (lo+hi)/2
    if sparse_g1(mid)<1:
        lo=mid
    else:
        hi=mid
s = (lo+hi)/2
g2 = math.fsum(w*n*(n-1)*s**(n-2) for n,w in degrees)
nmin = 2**32
log_tail_bound = (math.log(nmin)+(nmin-1)*math.log(s))/math.log(10)
print(f"infinite-log sparse law: s*={s:.12f}, rho={1+(1-s)*g2:.12f}; omitted G' tail <10^({log_tail_bound:.0f})")
print("sparse normalization telescopes; E log N = log(2) sum 2^j/[j(j+1)] = infinity")

print("\nTWO-STATE IDENTITY AND MOMENTS")
for p in [F(0),F(1,4),F(1,2),F(9,10),F(1)]:
    cutoff=80
    direct=sum((p**n+n*(1-p)*p**(n-1))/F(n*(n-1)) for n in range(2,cutoff+1))
    telescoped=p-p**cutoff/cutoff
    assert direct == telescoped
    print(f"p={p}: partial Psi_80 = p-p^80/80 EXACT PASS")
cutoff=100000
mean_partial=math.fsum(1/(n-1) for n in range(2,cutoff+1))
log_partial=math.fsum(math.log1p(n)/(n*(n-1)) for n in range(2,cutoff+1))
# For n>=cutoff+1: 1/[n(n-1)] <= 2/n^2 and log(1+n)<=log(2n).
log_tail=2*(math.log(2*cutoff)+1)/cutoff
print(f"mean partial through {cutoff}: {mean_partial:.12f} (harmonic, divergent)")
print(f"E log(1+N) partial={log_partial:.12f}; remaining <= {log_tail:.12f} (finite)")

print("\nFINITE-EXPLORATION SPINE CHECK (leaf/binary law)")
# chi(0)=1/4, chi(2)=3/4, s=2/3. b-pivotal ray is immortal.
# Survival from a solves r=1/2*(1-(1-r)^2)+1/8, hence r=1/2.
s=2/3
p=1-s
ra=.5
rb=1.
records={0:[],1:[]}
for n,cn in [(0,.25),(2,.75)]:
    for children in itertools.product(range(2),repeat=n):
        parent=automaton(children)
        col_weight=cn*math.prod(p if c else s for c in children)
        for survives in itertools.product(range(2),repeat=n):
            weight=col_weight*math.prod((rb if c else ra) if q else (1-(rb if c else ra))
                                       for c,q in zip(children,survives))
            surviving_pivots=[]
            for j,c in enumerate(children):
                switched=list(children)
                switched[j]=1-c
                if survives[j] and automaton(switched)!=parent:
                    surviving_pivots.append(j)
            if not surviving_pivots:
                continue
            records[parent].append((children,survives,surviving_pivots,weight))
survival_mass=[s*ra,p*rb]
cvals=[]
for parent in (0,1):
    normalization=sum(rec[3] for rec in records[parent])
    assert abs(normalization-survival_mass[parent])<1e-14
    cval=sum(rec[3]/len(rec[2]) for rec in records[parent])/normalization
    cvals.append(cval)
print(f"survival probabilities: a={ra:.12f}, b=1; conditional E[W]: a={cvals[0]:.12f}, b={cvals[1]:.12f}")
for parent in (0,1):
    pair=0.
    for children,survives,pivs,weight in records[parent]:
        pair += weight/survival_mass[parent]/len(pivs)*sum(cvals[children[j]] for j in pivs)/len(pivs)
    assert pair < 1
    print(f"conditional E[W_i W_(i+1)] from {'b' if parent else 'a'}s={pair:.12f}<1 PASS")
print("Selecting a surviving child uses its label and independent choice only; unrevealed subtree retains its conditional RST law.")

print("\nFULL-SPINE CONDITIONING COUNTERCHECK (binary XOR)")
# On delta_2 the pivot tree is the whole tree and all s-labels are certain.
# Condition the original root to be a; its children are aa or bb equally.
# After switching a uniformly selected child the root is b. G_1 already
# determines the first child's colour, unlike RST_bs (probability 1/2).
for children in [(0,0),(1,1)]:
    for chosen in (0,1):
        switched=list(children)
        switched[chosen]=1-switched[chosen]
        conditional_indicator=int(switched[0]==1)
        print(f"original={children}, chosen={chosen}, switched={tuple(switched)}: P(first child b | G)={conditional_indicator}, RST_bs=0.5")
        assert conditional_indicator != .5
# Check regeneration at H_1 by enumerating depth two under original root a.
histograms={}
for leaves in itertools.product(range(2),repeat=4):
    children=(automaton(leaves[:2]),automaton(leaves[2:]))
    if automaton(children)!=0:
        continue
    for chosen in (0,1):
        history=(children,chosen)
        grand=tuple(leaves[2*chosen:2*chosen+2])
        histograms.setdefault(history,{})
        histograms[history][grand]=histograms[history].get(grand,F(0))+F(1,16)
for (children,chosen),hist in histograms.items():
    total=sum(hist.values())
    assert len(hist)==2 and all(weight/total==F(1,2) for weight in hist.values())
    assert all(automaton(grand)==children[chosen] for grand in hist)
print("All four finite exploration histories retain the correct conditional subtree law: EXACT PASS")

print("\nALL CHECKS PASSED")
print(f"elapsed_seconds={time.monotonic()-started:.3f}")
print(f"peak_RSS_MiB={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2):.2f} (macOS bytes)")
