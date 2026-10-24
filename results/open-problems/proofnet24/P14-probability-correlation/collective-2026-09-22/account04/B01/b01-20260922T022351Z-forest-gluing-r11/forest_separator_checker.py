from fractions import Fraction
from itertools import combinations
import random

def forest(V, S):
    p={v:v for v in V}
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in S:
        a,b=f(a),f(b)
        if a==b:return False
        p[b]=a
    return True

def conn(V,S,s="u",t="v"):
    A={v:[] for v in V}
    for a,b in S:A[a].append(b);A[b].append(a)
    q=[s];z={s}
    while q:
        x=q.pop()
        if x==t:return True
        for y in A[x]:
            if y not in z:z.add(y);q.append(y)
    return False

def P(V,E,w,sep=False):
    r={k:Fraction(0) for k in ("T","D","C")}
    for k in ("T1","D1","C1","T2","D2","C2"):r[k]={}
    for m in range(1<<len(E)):
        S=[E[i] for i in range(len(E)) if m>>i&1]
        if not forest(V,S):continue
        x=Fraction(1)
        for e in S:x*=w[e]
        q="C" if sep and conn(V,S) else ("D" if sep else "T")
        if sep:r["T"]+=x
        r[q]+=x
        for e in S:
            r[q+"1"][e]=r[q+"1"].get(e,0)+x/w[e]
            if sep:r["T1"][e]=r["T1"].get(e,0)+x/w[e]
        for e,f in combinations(S,2):
            k=tuple(sorted((e,f)))
            r[q+"2"][k]=r[q+"2"].get(k,0)+x/(w[e]*w[f])
            if sep:r["T2"][k]=r["T2"].get(k,0)+x/(w[e]*w[f])
    return r

def bridge(g,i):
    X=[f"{i}x{k}" for k in range(g.randint(1,2))]
    V=["u","v"]+X; E=set()
    path=["u"]+X+["v"]
    for a,b in zip(path,path[1:]):E.add(tuple(sorted((a,b))))
    C=[tuple(sorted(x)) for x in combinations(V,2)]
    C=[e for e in C if e not in E and e!=("u","v")]
    g.shuffle(C)
    for e in C[:g.randint(0,min(1,len(C)))]:E.add(e)
    E=sorted(E);w={e:Fraction(g.randint(1,4)) for e in E}
    return V,E,w

g=random.Random(20260922); checks=0
for case in range(24):
    B=[];V={"u","v"};E=[];w={}
    for i in range(g.randint(2,3)):
        v,e,a=bridge(g,i);B.append((v,e,a));V.update(v);E+=e;w.update(a)
    if case%3==0:
        e=("u","v");a={e:Fraction(g.randint(1,4))}
        B.append((["u","v"],[e],a));E.append(e);w.update(a)
    G=P(sorted(V),E,w);Q=[P(v,e,a,True) for v,e,a in B]
    prod=Fraction(1)
    for q in Q:prod*=q["D"]
    I=prod
    for i,q in enumerate(Q):
        A=Fraction(1)
        for j,s in enumerate(Q):
            if i!=j:A*=s["D"]
        I+=q["C"]*A
    assert I==G["T"]
    loc={}
    for i,(_,es,_) in enumerate(B):
        for e in es:loc[e]=i
    for e,f in combinations(E,2):
        k=tuple(sorted((e,f)))
        actual=G["T1"].get(e,0)*G["T1"].get(f,0)-G["T"]*G["T2"].get(k,0)
        i,j=loc[e],loc[f]
        if i==j:
            A=Fraction(1);lam=Fraction(0)
            for h,s in enumerate(Q):
                if h!=i:A*=s["D"];lam+=s["C"]/s["D"]
            q=Q[i];J=q["C"]+(1+lam)*q["D"]
            Je=q["C1"].get(e,0)+(1+lam)*q["D1"].get(e,0)
            Jf=q["C1"].get(f,0)+(1+lam)*q["D1"].get(f,0)
            Jef=q["C2"].get(k,0)+(1+lam)*q["D2"].get(k,0)
            pred=A*A*(Je*Jf-J*Jef)
        else:
            A=Fraction(1)
            for h,s in enumerate(Q):
                if h not in (i,j):A*=s["D"]
            qi,qj=Q[i],Q[j]
            Ri=qi["D"]*qi["C1"].get(e,0)-qi["C"]*qi["D1"].get(e,0)
            Rj=qj["D"]*qj["C1"].get(f,0)-qj["C"]*qj["D1"].get(f,0)
            pred=A*A*Ri*Rj
        assert actual==pred
        checks+=1
print("PASS")
print("cases",24)
print("marked_pair_identities",checks)
print("seed",20260922)
