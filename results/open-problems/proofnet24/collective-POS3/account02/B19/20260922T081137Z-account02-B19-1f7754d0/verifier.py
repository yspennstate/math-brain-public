#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction
from itertools import combinations

def closure(n, edges):
    r=[[False]*n for _ in range(n)]
    for u,v in edges: r[u][v]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]: r[i][j]=True
    assert not any(r[i][i] for i in range(n))
    return r

def preds(r):
    n=len(r); p=[0]*n
    for v in range(n):
        for u in range(n):
            if r[u][v]: p[v] |= 1<<u
    return p

def counter(p):
    n=len(p); full=(1<<n)-1
    @lru_cache(None)
    def f(mask):
        if mask==full: return 1
        s=0
        for x in range(n):
            if not (mask>>x)&1 and not (p[x] & ~mask):
                s += f(mask | (1<<x))
        return s
    return f

def pair_count(p,u,v):
    q=p.copy(); q[v] |= 1<<u
    return counter(q)(0)

def incomparable_pairs(r,p):
    E=counter(p)(0); out=[]
    for u,v in combinations(range(len(r)),2):
        if not r[u][v] and not r[v][u]:
            n=pair_count(p,u,v)
            out.append((u,v,n,E))
    return out

def connected_incomp(r):
    n=len(r); adj=[[] for _ in range(n)]
    for u,v in combinations(range(n),2):
        if not r[u][v] and not r[v][u]:
            adj[u].append(v); adj[v].append(u)
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); st.append(v)
    return len(seen)==n

def autonomous_nontrivial(r):
    n=len(r); out=[]
    for mask in range(1,(1<<n)-1):
        if mask & (mask-1)==0: continue
        A=[i for i in range(n) if (mask>>i)&1]
        ok=True
        for z in range(n):
            if (mask>>z)&1: continue
            typ=set()
            for a in A:
                typ.add(-1 if r[z][a] else (1 if r[a][z] else 0))
            if len(typ)>1:
                ok=False; break
        if ok: out.append(tuple(A))
    return out

def family(m):
    labels=[0,1,2,3,4]+[f"c{i+1}" for i in range(m)]+[7,8,9,10]
    I={x:i for i,x in enumerate(labels)}
    e=[]
    def add(a,b): e.append((I[a],I[b]))
    add(0,1); add(0,7); add(1,2); add(2,3); add(4,1)
    add(4,"c1")
    for i in range(m-1): add(f"c{i+1}",f"c{i+2}")
    add(f"c{m}",7); add(f"c{m}",10)
    add(7,2); add(8,4); add(8,9); add(9,3); add(9,10)
    r=closure(len(labels),e); p=preds(r)
    return labels,I,e,r,p

def quotient_m2_is_m1():
    lab2,I2,e2,r2,p2=family(2)
    lab1,I1,e1,r1,p1=family(1)
    groups=[]
    for x in lab1:
        if x=="c1": groups.append([I2["c1"],I2["c2"]])
        else: groups.append([I2[x]])
    for i,G in enumerate(groups):
        for j,H in enumerate(groups):
            if i==j: continue
            qrel=any(r2[u][v] for u in G for v in H)
            assert qrel==r1[i][j]
    return True

def grid(m,k=3):
    lab=[(i,j) for i in range(m) for j in range(k)]
    n=len(lab)
    e=[]
    for u,(i,j) in enumerate(lab):
        for v,(a,b) in enumerate(lab):
            if (a==i+1 and b==j) or (a==i and b==j+1):
                e.append((u,v))
    r=closure(n,e); p=preds(r)
    return lab,r,p

def iscover_grid(a,b):
    return a[0]<=b[0] and a[1]<=b[1] and a!=b and (b[0]-a[0])+(b[1]-a[1])==1

def grid_coherent_count(m):
    lab,r,p=grid(m); E=counter(p)(0)
    P={}
    for u,v,n,D in incomparable_pairs(r,p):
        P[(u,v)]=Fraction(n,D); P[(v,u)]=1-P[(u,v)]
    def comp(u,v): return u==v or r[u][v] or r[v][u]
    good=0
    for x in range(len(lab)):
      for y in range(len(lab)):
        if not iscover_grid(lab[x],lab[y]): continue
        for a in range(len(lab)):
          if comp(a,x) or comp(a,y): continue
          if P.get((x,a),0)<=Fraction(2,3) or P.get((a,y),0)<=Fraction(2,3): continue
          for rl in range(len(lab)):
            if not iscover_grid(lab[x],lab[rl]): continue
            if comp(rl,a) or comp(rl,y) or P.get((y,rl),0)<=Fraction(2,3): continue
            for rr in range(len(lab)):
              if not iscover_grid(lab[a],lab[rr]): continue
              if comp(rr,y) or P.get((y,rr),0)<=Fraction(2,3): continue
              if comp(rl,rr) or P.get((rl,rr),0)<=Fraction(2,3): continue
              good += 1
    return E,good

def show_family(m):
    lab,I,e,r,p=family(m); E=counter(p)(0)
    A=[I[x] for x in [0,1,2,3]]
    B=[I[4]]+[I[f"c{i+1}"] for i in range(m)]+[I[7]]
    C=[I[x] for x in [8,9,10]]
    assert all(r[a][b] for chain in [A,B,C] for a,b in zip(chain,chain[1:]))
    tri=[I[x] for x in [0,4,9]]
    assert all(not r[u][v] and not r[v][u] for u,v in combinations(tri,2))
    assert connected_incomp(r)
    gate=[(0,9),(9,1),(1,7),(1,10),(7,10)]
    g=[]
    for a,b in gate:
        n=pair_count(p,I[a],I[b]); g.append((a,b,n,E))
    print(f"P_{m}: n={len(lab)} E={E} width=3 connected_incomp=True")
    print("  gate_counts " + ", ".join(f"{a}<{b}:{n}/{E}" for a,b,n,E in g))
    print("  gate_gt_2/3 " + str([3*n>2*E for a,b,n,E in g]))
    autos=autonomous_nontrivial(r)
    print("  autonomous_nontrivial=" + str([tuple(lab[i] for i in A) for A in autos]))
    return lab,I,r,p,E,g

lab1,I1,r1,p1,E1,g1=show_family(1)
lab2,I2,r2,p2,E2,g2=show_family(2)
assert E1==299 and E2==533
assert [n for _,_,n,_ in g1]==[221,204,185,244,230]
assert [n for _,_,n,_ in g2]==[389,360,364,448,408]
assert [3*n>2*E1 for _,_,n,_ in g1]==[True,True,False,True,True]
assert all(3*n>2*E2 for _,_,n,_ in g2)
assert autonomous_nontrivial(r1)==[]
assert [tuple(lab2[i] for i in A) for A in autonomous_nontrivial(r2)]==[("c1","c2")]
assert quotient_m2_is_m1()
print("CONTRACTION P_2/{c1,c2} == P_1: True")

pairs=incomparable_pairs(r2,p2)
print(f"P_2 incomparable_pairs={len(pairs)}")
balanced=[]
for u,v,n,D in pairs:
    q=Fraction(n,D)
    bal=(3*n>=D and 3*n<=2*D)
    if bal: balanced.append((lab2[u],lab2[v],q))
    print(f"  {lab2[u]}||{lab2[v]}  Pr({lab2[u]}<{lab2[v]})={q.numerator}/{q.denominator} balanced={bal}")
assert len(pairs)==19
assert len(balanced)==5
print("P_2 balanced_pairs=" + str([(a,b,f"{q.numerator}/{q.denominator}") for a,b,q in balanced]))

for m in range(3,8):
    E,g=grid_coherent_count(m)
    print(f"GRID C_{m}xC_3 E={E} coherent_F1_F3_patterns={g}")
    assert g==0

print("POS3_COHERENT_GATE_MODULE_PHASE_PASS")
