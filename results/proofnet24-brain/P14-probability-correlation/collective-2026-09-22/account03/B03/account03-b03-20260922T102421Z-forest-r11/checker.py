#!/usr/bin/env python3
from itertools import combinations

def dsu_forest(n, edges):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v,_ in edges:
        a,b=find(u),find(v)
        if a==b:
            return False
        p[a]=b
    return True

def term_partition(n, edges, terms):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v,_ in edges:
        a,b=find(u),find(v)
        if a!=b: p[a]=b
    groups={}
    for t in terms:
        groups.setdefault(find(t),[]).append(t)
    return tuple(sorted((tuple(sorted(g)) for g in groups.values()), key=lambda z:z[0]))

def weighted_partition_masses(n, edge_list, terms):
    out={}
    m=len(edge_list)
    for mask in range(1<<m):
        sub=[edge_list[i] for i in range(m) if mask>>i&1]
        if not dsu_forest(n,sub): continue
        wt=1
        for _,_,w in sub: wt*=w
        pi=term_partition(n,sub,terms)
        out[pi]=out.get(pi,0)+wt
    return out

def weighted_gap(n, edge_list, mark_e, mark_f):
    z=ze=zf=zef=0
    m=len(edge_list)
    for mask in range(1<<m):
        sub=[edge_list[i] for i in range(m) if mask>>i&1]
        if not dsu_forest(n,sub): continue
        wt=1
        for _,_,w in sub: wt*=w
        z+=wt
        ie=(mask>>mark_e)&1; jf=(mask>>mark_f)&1
        if ie: ze+=wt
        if jf: zf+=wt
        if ie and jf: zef+=wt
    return ze*zf-z*zef

# weighted cubic lifting identity
ALL=((0,1,2),)
U=((0,),(1,2))
V=((0,1),(2,))
W=((0,2),(1,))
DISC=((0,),(1,),(2,))
weights=[2,3,5,7,11,13]
all4=list(combinations(range(4),2))
checked_cubic=0
min_q2=None
for hmask in range(1<<len(all4)):
    H=[]
    for i,(u,v) in enumerate(all4):
        if hmask>>i&1:
            H.append((u,v,weights[i]))
    masses=weighted_partition_masses(4,H,(0,1,2))
    A=masses.get(ALL,0); Uv=masses.get(U,0); Vv=masses.get(V,0)
    Wv=masses.get(W,0); C=masses.get(DISC,0)
    T=A+Uv+Vv+Wv+C
    q0=(A+Vv)*T
    q1=2*Vv*T
    q2=-A*C + Uv*Vv + Uv*Wv + Vv*Vv + Vv*Wv + Vv*C
    for c in (1,2,5):
        G=H+[(4,0,2),(4,1,3),(4,2,c)]
        direct=weighted_gap(5,G,len(H),len(H)+1)
        formula=2*3*(q0+q1*c+q2*c*c)
        assert direct==formula, (hmask,c,direct,formula)
        checked_cubic+=1
    Gc=H+[(2,0,2),(2,1,3)]
    contr=weighted_gap(4,Gc,len(H),len(H)+1)
    assert contr==2*3*q2, (hmask,contr,6*q2)
    min_q2=q2 if min_q2 is None else min(min_q2,q2)

# degree-4 finite-difference boundary test
def canonical_parts4():
    def rec(seq):
        if not seq:
            yield ()
            return
        x=seq[0]
        for p in rec(seq[1:]):
            yield ((x,),)+p
            for i in range(len(p)):
                q=list(p); q[i]=tuple(sorted((x,)+q[i]))
                yield tuple(sorted(q,key=lambda b:b[0]))
    return sorted(set(rec((0,1,2,3))), key=lambda p:(len(p),p))
P4=canonical_parts4()
PI={p:i for i,p in enumerate(P4)}

def forest_partition_from_mask(n, mask, edges):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if mask>>i&1:
            a,b=find(u),find(v)
            if a==b: return None
            p[a]=b
    groups={}
    for t in range(4):
        groups.setdefault(find(t),[]).append(t)
    return tuple(sorted((tuple(g) for g in groups.values()), key=lambda z:z[0]))

def star_response(pi, x, y):
    star=[(0,1),(1,1),(2,x),(3,y)]
    z=ze=zf=zef=0
    for sm in range(16):
        seen=set(); ok=True; wt=1
        for i,(t,w) in enumerate(star):
            if not (sm>>i)&1: continue
            if w==0: wt=0; break
            bi=next(j for j,B in enumerate(pi) if t in B)
            if bi in seen: ok=False; break
            seen.add(bi); wt*=w
        if not ok or wt==0: continue
        z+=wt
        if sm&1: ze+=wt
        if sm&2: zf+=wt
        if (sm&1) and (sm&2): zef+=wt
    return z,ze,zf,zef

RESP={(i,x,y):star_response(p,x,y) for i,p in enumerate(P4)
      for x in (0,1) for y in (0,1)}

def gap_from_counts(counts,x,y):
    z=ze=zf=zef=0
    for i,nc in enumerate(counts):
        a,b,c,d=RESP[(i,x,y)]
        z+=nc*a; ze+=nc*b; zf+=nc*c; zef+=nc*d
    return ze*zf-z*zef

def quadratic_coeffs(evalfun):
    diag=[evalfun([1 if k==i else 0 for k in range(15)]) for i in range(15)]
    coeff=[]
    for i in range(15):
        coeff.append(diag[i])
        for j in range(i+1,15):
            c=[0]*15; c[i]=1; c[j]=1
            coeff.append(evalfun(c)-diag[i]-diag[j])
    return coeff

def sign_summary(vals):
    return (sum(v>0 for v in vals),sum(v<0 for v in vals),sum(v==0 for v in vals),
            min(vals),max(vals))

def evalF(counts,x,y):
    return gap_from_counts(counts,x,y)
def evalM(counts):
    return evalF(counts,1,1)-evalF(counts,1,0)-evalF(counts,0,1)+evalF(counts,0,0)
def evalR(counts):
    return evalF(counts,1,0)+evalF(counts,0,1)-evalF(counts,0,0)

coef_stats={
    "F00":sign_summary(quadratic_coeffs(lambda c:evalF(c,0,0))),
    "F10":sign_summary(quadratic_coeffs(lambda c:evalF(c,1,0))),
    "F01":sign_summary(quadratic_coeffs(lambda c:evalF(c,0,1))),
    "F11":sign_summary(quadratic_coeffs(lambda c:evalF(c,1,1))),
    "M":sign_summary(quadratic_coeffs(evalM)),
    "R":sign_summary(quadratic_coeffs(evalR)),
}

edges6=list(combinations(range(6),2))
m=len(edges6); size=1<<m
arr=[[0]*size for _ in range(15)]
for mask in range(size):
    p=forest_partition_from_mask(6,mask,edges6)
    if p is not None:
        arr[PI[p]][mask]=1
for bit in range(m):
    step=1<<bit
    for base in range(0,size,2*step):
        for off in range(step):
            lo=base+off; hi=lo+step
            for p in range(15):
                arr[p][hi]+=arr[p][lo]

stat={k:{"neg":0,"zero":0,"minpos":None,"max":None} for k in ("M","R","F11")}
for Hmask in range(size):
    counts=[arr[p][Hmask] for p in range(15)]
    F00=gap_from_counts(counts,0,0)
    F10=gap_from_counts(counts,1,0)
    F01=gap_from_counts(counts,0,1)
    F11=gap_from_counts(counts,1,1)
    M=F11-F10-F01+F00
    R=F10+F01-F00
    for key,val in (("M",M),("R",R),("F11",F11)):
        if val<0: stat[key]["neg"]+=1
        elif val==0: stat[key]["zero"]+=1
        else:
            z=stat[key]["minpos"]
            stat[key]["minpos"]=val if z is None else min(z,val)
        z=stat[key]["max"]
        stat[key]["max"]=val if z is None else max(z,val)

assert checked_cubic==64*3
assert all(stat[k]["neg"]==0 for k in stat)
print("FOREST-CUBIC-LIFT-v1")
print("weighted_cubic_host_graphs=64")
print("weighted_cubic_activity_checks=192")
print("weighted_cubic_contraction_identity_checks=64")
print("min_observed_q2=%d" % min_q2)
print("FOREST-DEG4-FINITE-DIFF-v1")
for key in ("F00","F10","F01","F11","M","R"):
    p,n,z,mi,ma=coef_stats[key]
    print("coeff_%s pos=%d neg=%d zero=%d min=%d max=%d" % (key,p,n,z,mi,ma))
print("six_vertex_boundary_hosts=32768")
for key in ("M","R","F11"):
    s=stat[key]
    print("%s neg=%d zero=%d minpos=%s max=%s" %
          (key,s["neg"],s["zero"],s["minpos"],s["max"]))
print("PASS")
