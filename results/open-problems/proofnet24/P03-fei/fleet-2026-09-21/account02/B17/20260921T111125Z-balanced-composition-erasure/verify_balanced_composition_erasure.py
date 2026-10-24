#!/usr/bin/env python3
from fractions import Fraction
from math import log2
from itertools import combinations
import json

TAU = 0.1805539925
K_HOD_SELECTOR = 3.5693936182

def h2(x):
    x=float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)

def walsh_probs(values):
    a=[int(v) for v in values]
    n=len(a)
    h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y
                a[j+h]=x-y
        h*=2
    return [Fraction(w*w,n*n) for w in a], a

def stats(probs, dim):
    H=sum(-float(p)*log2(float(p)) for p in probs if p)
    infl=[]; erase=[]; singleton=[]
    for i in range(dim):
        pi=sum((p for mask,p in enumerate(probs) if (mask>>i)&1), Fraction())
        groups={}
        for mask,p in enumerate(probs):
            rest=mask & ~(1<<i)
            bit=(mask>>i)&1
            groups.setdefault(rest,[Fraction(),Fraction()])[bit]+=p
        Bi=0.0
        for q0,q1 in groups.values():
            t=q0+q1
            if q0 and q1:
                Bi += float(t)*h2(q1/t)
        infl.append(pi); erase.append(Bi); singleton.append(probs[1<<i])
    return H,sum(infl,Fraction()),infl,erase,singleton

def outer_and3(z):
    return -1 if z[0]==z[1]==z[2]==1 else 1

def phi(alpha, rr):
    aa=float(alpha); rrf=float(rr)
    return h2(aa)+aa*h2(rrf)-h2(aa*(1-rrf))

# Outer AND_3. Input encoding only changes Fourier signs, not squared spectrum.
Fvals=[]
for idx in range(8):
    z=tuple(1 if ((idx>>i)&1)==0 else -1 for i in range(3))
    Fvals.append(outer_and3(z))
Fprobs,FW=walsh_probs(Fvals)
HF,IF,a,BF,rF=stats(Fprobs,3)
assert IF == Fraction(3,4)
assert a == [Fraction(1,4)]*3
outer_K=[BF[i]/float(a[i]) for i in range(3)]

groups_outer={}
for mask,p in enumerate(Fprobs):
    rest=mask & ~1
    bit=mask&1
    groups_outer.setdefault(rest,[Fraction(),Fraction()])[bit]+=p

def composition_coordinate(q,B,r):
    eph=0.0
    for q0,q1 in groups_outer.values():
        t=q0+q1
        if t:
            eph += float(t)*phi(q1/t,r)
    p=a[0]*q
    Bout=float(a[0])*B+eph
    return p,Bout,Bout/float(p),eph

# Exhaust all balanced 4-bit inner Boolean functions modulo global sign.
best_score=-1.0
best_plus=None
best_stats=None
valid=0
tested=0
for plus_tuple in combinations(range(16),8):
    if 0 in plus_tuple:
        continue
    tested += 1
    plus=set(plus_tuple)
    vals=[1 if i in plus else -1 for i in range(16)]
    probs,W=walsh_probs(vals)
    H,I,q,B,r=stats(probs,4)
    rows=[]
    ok=True
    for u in range(4):
        if q[u]==0:
            continue
        p,Bc,K,eph=composition_coordinate(q[u],B[u],r[u])
        if float(p) >= TAU:
            ok=False
            break
        rows.append((u,p,Bc,K,eph))
    if not ok or not rows:
        continue
    valid += 1
    score=min(row[3] for row in rows)
    if score > best_score + 1e-13:
        best_score=score
        best_plus=tuple(sorted(plus))
        best_stats=(H,I,q,B,r,W,rows)

assert tested == 6435
assert best_plus is not None

Hg,Ig,q,Bg,r,gW,rows=best_stats
PLUS=set(best_plus)
gvals=[1 if i in PLUS else -1 for i in range(16)]
gprobs,_=walsh_probs(gvals)
inner_K=[Bg[i]/float(q[i]) for i in range(4) if q[i]]
assert all(r[i] <= q[i]*q[i] for i in range(4))

# Direct 12-bit Boolean composition for the finite counterexample/extremizer.
hvals=[]
for idx in range(1<<12):
    z=[]
    for block in range(3):
        local=(idx>>(4*block)) & 15
        z.append(1 if local in PLUS else -1)
    hvals.append(outer_and3(tuple(z)))
hprobs,hW=walsh_probs(hvals)
Hh,Ih,ph,Bh,rh=stats(hprobs,12)
pred=[composition_coordinate(q[u],Bg[u],r[u]) for u in range(4)]
for block in range(3):
    for u in range(4):
        k=4*block+u
        pp,bb,kk,eph=pred[u]
        assert ph[k] == pp
        assert abs(Bh[k]-bb) < 2e-12
assert abs(Hh-(HF+float(IF)*Hg)) < 2e-12
assert Ih == IF*Ig

comp_K=[Bh[i]/float(ph[i]) for i in range(12) if ph[i]]
max_parent=max(max(outer_K),max(inner_K))
assert min(comp_K) > max_parent
assert min(comp_K) <= K_HOD_SELECTOR

# Proved comparison bound: K_comp <= K_inner + q*K_outer + h(q^2)/q
comparison_bounds=[]
for u in range(4):
    if not q[u]:
        continue
    ku=Bg[u]/float(q[u])
    rhs=ku + float(q[u])*outer_K[0] + h2(float(q[u]*q[u]))/float(q[u])
    comparison_bounds.append({"u":u,"actual":pred[u][2],"bound":rhs})
    assert pred[u][2] <= rhs + 1e-12

out={
  "status":"PASS",
  "normalization":"uniform cube; log2 entropy; Fourier probabilities are squared normalized Walsh coefficients",
  "search":{
    "balanced_4bit_functions_tested_mod_global_sign":tested,
    "valid_low_influence_compositions":valid,
    "outer":"AND_3",
    "maximized_quantity":"minimum physical-coordinate B_i/Inf_i after composition, subject to every relevant physical influence < tau",
    "best_min_erasure_ratio":best_score,
    "Hod_scale_selector_target":K_HOD_SELECTOR,
    "gap_to_Hod_selector_target":K_HOD_SELECTOR-best_score,
    "selector_target_refuted":best_score > K_HOD_SELECTOR
  },
  "extremal_inner":{
    "truth_plus_indices_0_to_15":list(best_plus),
    "balanced":sum(gvals)==0,
    "walsh_integer_coefficients_nonzero":{str(i):w for i,w in enumerate(gW) if w},
    "H":Hg,"I":float(Ig),"H_over_I":Hg/float(Ig),
    "influences":[float(x) for x in q],
    "erasure_entropies":Bg,
    "erasure_ratios":[Bg[i]/float(q[i]) if q[i] else None for i in range(4)],
    "singleton_spectral_weights":[float(x) for x in r],
    "r_le_q_squared":[bool(r[i] <= q[i]*q[i]) for i in range(4)]
  },
  "outer_AND3":{
    "H":HF,"I":float(IF),"H_over_I":HF/float(IF),
    "influences":[float(x) for x in a],
    "erasure_ratios":outer_K
  },
  "composition_12bit":{
    "H":Hh,"I":float(Ih),"H_over_I":Hh/float(Ih),
    "physical_influences":[float(x) for x in ph],
    "max_physical_influence":max(float(x) for x in ph),
    "tau":TAU,
    "all_relevant_physical_influences_below_tau":all(float(x)<TAU for x in ph if x),
    "erasure_ratios":comp_K,
    "min_erasure_ratio":min(comp_K),
    "max_parent_erasure_ratio":max_parent,
    "max_parent_closure_refuted":min(comp_K)>max_parent,
    "Hod_selector_target_refuted":min(comp_K)>K_HOD_SELECTOR
  },
  "comparison_bounds":comparison_bounds
}
print(json.dumps(out,indent=2,sort_keys=True))
