"""Exact finite checks for scalar jets and the preceding hierarchy lemma.
No SK simulation, external package, numerical diffusion, or Lean build.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import itertools
import json
import math
import os
import re
import resource
import sys
import time

start = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15
root = Path(__file__).resolve().parent
out = {"effective_niceness": priority}

# Sparse polynomials (time, z_A, z_B), with exact rational coefficients.
# Retain time degree <= 2 and spatial degree <= 8 throughout.
def clean(p):
    return {e: v for e, v in p.items() if v and e[0] <= 2 and sum(e[1:]) <= 8}

def add(*polys):
    p = {}
    for q in polys:
        for e, v in q.items():
            p[e] = p.get(e, Q(0)) + v
    return clean(p)

def scale(p, a):
    return clean({e: v*a for e, v in p.items()})

def mul(p, q):
    r = {}
    for e, v in p.items():
        for f, w in q.items():
            g = tuple(x+y for x, y in zip(e, f))
            if g[0] <= 2 and sum(g[1:]) <= 8:
                r[g] = r.get(g, Q(0)) + v*w
    return clean(r)

def deriv(p, i):
    r = {}
    for e, v in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            r[tuple(f)] = v*e[i]
    return clean(r)

def shift(p, n):
    return clean({(e[0]+n,e[1],e[2]):v for e,v in p.items()})

def spatial_zero(p):
    return {e: v for e, v in p.items() if e[1:] == (0,0)}

def time_zero(p):
    return {e: v for e,v in p.items() if e[0] == 0}

def generator(p, k, shared, M_A=None, M_B=None):
    diff = add(deriv(deriv(p,1),1),deriv(deriv(p,2),2))
    if shared:
        diff = add(diff,scale(deriv(deriv(p,1),2),2))
    result = scale(diff,k/2)
    if M_A is not None:
        result = add(result,mul(M_A,deriv(p,1)),mul(M_B,deriv(p,2)))
    return result


def jet_case(chi,g,h,k0,k1,r):
    # Formal PDE solve, from arbitrary even initial jets through z^8.
    G = {(0,2,0):chi/2,(0,4,0):g/24,(0,6,0):h/720,
         (0,8,0):Q(11,40320)}
    kval = {(0,0,0):k0,(1,0,0):k1}
    for tdegree in range(2):
        M = deriv(G,1)
        rhs = scale(mul(kval,add(deriv(M,1),shift(mul(M,M),1))),Q(-1,2))
        nxt = {(tdegree+1,e[1],e[2]):v/(tdegree+1)
               for e,v in rhs.items() if e[0] == tdegree}
        G = add(G,nxt)
    M = deriv(G,1)
    P_A = add(deriv(M,1),shift(mul(M,M),1))
    P_B = {(e[0],e[2],e[1]):v for e,v in P_A.items()}
    f = mul(P_A,P_B)
    M0_A = time_zero(M)
    M0_B = {(e[0],e[2],e[1]):v for e,v in M0_A.items()}
    def L(p,shared):
        return generator(p,k0,shared)
    def Lprime(p,shared):
        return generator(p,k1,shared,scale(M0_A,k0),scale(M0_B,k0))
    # Time-ordered generator series: shared on [0,rc], independent after rc.
    result = add(
        spatial_zero(f),
        shift(spatial_zero(add(scale(L(f,True),r),scale(L(f,False),1-r))),1),
        shift(spatial_zero(add(scale(Lprime(f,True),r*r/2),
                              scale(Lprime(f,False),(1-r*r)/2))),2),
        shift(spatial_zero(add(scale(L(L(f,True),True),r*r/2),
                              scale(L(L(f,False),True),r*(1-r)),
                              scale(L(L(f,False),False),(1-r)**2/2))),2))
    expected = {(0,0,0):chi**2,
                (2,0,0):chi**3*k0+g*g*k0*k0*r*r/2}
    assert result == clean(expected),(chi,g,h,k0,k1,r,result,expected)
    # Independent one-branch expansion for the mean of P.
    mean = add(spatial_zero(P_A),
               shift(spatial_zero(L(P_A,False)),1),
               shift(spatial_zero(scale(add(Lprime(P_A,False),
                                            L(L(P_A,False),False)),Q(1,2))),2))
    assert mean == {(0,0,0):chi,(2,0,0):chi*chi*k0/2},mean
    return {str(e[0]):str(v) for e,v in sorted(result.items())}

cases = []
for chi,g,h,k0,k1 in (
    (Q(1),Q(-2),Q(16),Q(2),Q(3)),
    (Q(3,2),Q(7,5),Q(-3),Q(5,4),Q(-2)),
    (Q(2),Q(0),Q(9),Q(1,3),Q(0)),
    (Q(1,7),Q(-3,2),Q(0),Q(7),Q(4))):
    for r in (Q(0),Q(1,1000000),Q(1,3),Q(1,2),Q(1)):
        coef = jet_case(chi,g,h,k0,k1,r)
        cases.append({"chi":str(chi),"g":str(g),"sixth_jet":str(h),
                      "k0":str(k0),"k1":str(k1),"v_over_c":str(r),
                      "E_P_A_P_B_coefficients_in_c":coef})
out["exact_generator_cases"] = cases

# The same pair covariance coefficient via Wick's formula, independently.
def wick(labels,cov):
    if not labels:
        return Q(1)
    if len(labels)%2:
        return Q(0)
    a,*rest = labels
    return sum((cov[a,b]*wick(rest[:i]+rest[i+1:],cov)
                for i,b in enumerate(rest)),Q(0))

wick_cases=0
for c in (Q(1,100),Q(1,10000)):
    for h in (Q(0),c/1000000,c/3,c):
        for later in (h,(c+h)/2,c):
            cov={(a,b):(c if a==b else
                         (later if {a,b}=={0,2} else h))
                 for a in range(3) for b in range(3)}
            error=wick([0,0,1,2],cov)-c*wick([1,2],cov)
            assert error==2*h*later
            assert abs(error)<=2*c*h
            pair_cov=wick([0,0,1,1],cov)-c*c
            assert pair_cov==2*h*h
            wick_cases+=1
out["wick_and_earlier_mass_cases"]=wick_cases

# Independent integer weight accounting for all five size monomials.
weights={"b":-2,"chi":1,"g":3,"k":-3}
monomials=[(2,{"b":2,"chi":3,"k":1}),
           (2,{"b":2,"g":2,"k":2}),
           (3,{"b":3,"g":2,"k":1}),
           (3,{"b":3,"chi":3}),
           (4,{"b":4,"g":2})]
scales=[]
for degree,powers in monomials:
    weight=sum(weights[t]*n for t,n in powers.items())
    assert weight==degree-6
    assert 1-Q(degree,6)+Q(weight,6)==0
    scales.append({"degree":degree,"weight":weight,"annihilator":"0"})
out["size_cancellation_weights"]=scales

# Independent exact finite hierarchy, with all masses equal to one.
# Two normalized future kernels; rational exp(H), with reciprocal gauge atoms.
spins=list(itertools.product((-1,1),repeat=3))
edges=list(itertools.combinations(range(3),2))
root_atoms=list(itertools.product((-1,1),repeat=3))
field_atoms=root_atoms
future_atoms=root_atoms
pinned=[Q(0)]*3
original=[Q(0)]*3
spin_mass=[Q(0)]*8
leaves=0
for root_edge in root_atoms:
    branches=[]
    for field in field_atoms:
        terminals=[]
        for future_edge in future_atoms:
            weights=[]
            for spin in spins:
                eroot=sum(e*spin[i]*spin[j] for e,(i,j) in zip(root_edge,edges))
                efuture=sum(e*spin[i]*spin[j] for e,(i,j) in zip(future_edge,edges))
                efield=sum(x*y for x,y in zip(field,spin))
                weights.append(Q(2)**eroot*Q(5)**efuture*Q(3)**efield)
            Z2=sum(weights)/8
            terminals.append((weights,Z2))
        Z1=sum(z for _,z in terminals)/8
        branches.append((terminals,Z1))
    Z0=sum(z for _,z in branches)/8
    for k in range(3):
        original[k]+=Z0**k/8
    for terminals,Z1 in branches:
        kernel1=Z1/(8*Z0)
        assert sum(z/(8*Z1) for _,z in terminals)==1
        for weights,Z2 in terminals:
            kernel2=Z2/(8*Z1)
            assert sum(w/(8*Z2) for w in weights)==1
            for i,w in enumerate(weights):
                joint=kernel1*kernel2*w/(8*Z2)/8
                spin_mass[i]+=joint
                if i==7:
                    for k in range(3):
                        pinned[k]+=8*joint*Z0**k
                leaves+=1
assert spin_mass==[Q(1,8)]*8
assert pinned==original
out["independent_hierarchy_recheck"]={
    "leaf_spin_cases":leaves,"uniform_spin_probabilities":"exactly 1/8",
    "pinned_continuation_tests":"1, exp(G), exp(2G): exact agreement",
    "future_transition_normalizations":"exact"}

# Distinct masses and terminal rescaling are a separate exact algebra check.
coef_cases=0
for terminal in (Q(1),Q(4)):
    for masses in ((Q(1,8),Q(1,3)),(Q(1,8),Q(1,8)),(terminal,terminal)):
        first,second=masses
        if second>terminal:
            continue
        raw=[-first,first-second,second-terminal]
        assert sum(raw)==-terminal
        rho=first/2
        assert all(x<=0 for x in [raw[0]+rho,*raw[1:]])
        assert (first-rho)/terminal==first/terminal-rho/terminal
        coef_cases+=1
out["hierarchy_coefficient_cases"]=coef_cases

# Fresh primary-source comparisons; only current-folder writes.
round4=Path("~/codex_op_1114r4/briefs/AV_T136")
comparison={}
for current,old in [("01-introduction.tex","limiting-law-introduction.tex"),
                    ("02-foundations.tex","limiting-law-foundations.tex"),
                    ("03-paths.tex","limiting-law-paths.tex"),
                    ("04-reduction.tex","limiting-law-reduction.tex"),
                    ("scale-introduction.tex","scale-introduction.tex"),
                    ("zero-temperature-main.tex","zero-temperature-main.tex"),
                    ("fluctuations-palomar-README.md","fluctuations-palomar-README.md")]:
    comparison[current]=((root/"sources"/current).read_text().rstrip("\n")==
                         (round4/"sources"/old).read_text().rstrip("\n"))
assert all(comparison.values()),comparison
out["fresh_sources_match_round4"]=comparison
verify=(root/"VERIFY.md").read_text()
fence=chr(96)*3
quotes=re.findall(fence+r"tex\n(.*?)\n"+fence,verify,re.S)
assert len(quotes)==5
for quote,name in zip(quotes,["01-introduction.tex"]*3+[
                               "scale-introduction.tex","zero-temperature-main.tex"]):
    assert quote in (root/"sources"/name).read_text(),name
out["verbatim_theorem_quotes"]=len(quotes)
for name in ("PROOF.md","VERIFY.md","REPORT.md","LOG.md"):
    s=(root/name).read_text()
    assert not any(ord(c)<32 and c not in "\n\t" for c in s),name
out["source_sha256"]={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in sorted((root/"sources").iterdir()) if p.is_file()}
out["elapsed_seconds"]=time.monotonic()-start
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out["peak_rss_bytes"]=rss if sys.platform=="darwin" else rss*1024
assert out["peak_rss_bytes"]<1024**3
assert out["elapsed_seconds"]<60
output=json.dumps(out,indent=2,ensure_ascii=False)
(root/"recheck_round5.txt").write_text(output+"\n")
print(output)

