#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict

def closure(n, rel):
    R=set(rel)
    changed=True
    while changed:
        changed=False
        add=set()
        for a,b in R:
            for c,d in R:
                if b==c and (a,d) not in R:
                    add.add((a,d))
        if add:
            R |= add
            changed=True
    return R

def covers(n, R):
    return sorted((a,b) for a,b in R
                  if not any((a,c) in R and (c,b) in R
                             for c in range(n) if c not in (a,b)))

def pred_succ(n,R):
    pred=[set() for _ in range(n)]
    succ=[set() for _ in range(n)]
    for a,b in R:
        succ[a].add(b); pred[b].add(a)
    return pred,succ

def width(n,R):
    comp=R|{(b,a) for a,b in R}
    best=0
    for r in range(1,n+1):
        for S in combinations(range(n),r):
            if all((x,y) not in comp for x,y in combinations(S,2)):
                best=r
    return best

def graph_connected(n, edges):
    adj=[set() for _ in range(n)]
    for x,y in edges:
        adj[x].add(y); adj[y].add(x)
    seen={0}; stack=[0]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return len(seen)==n

def linear_extensions(n,R):
    pm=[0]*n
    for x,y in R: pm[y] |= 1<<x
    full=(1<<n)-1
    ans=[]
    def rec(mask, out):
        if mask==full:
            ans.append(tuple(out)); return
        for v in range(n):
            if not ((mask>>v)&1) and (pm[v] & ~mask)==0:
                out.append(v); rec(mask|(1<<v),out); out.pop()
    rec(0,[])
    return ans

def before(e,x,y):
    return e.index(x)<e.index(y)

def count_before(exts,x,y):
    return sum(before(e,x,y) for e in exts)

def canonical(n,R,a,b):
    pred,succ=pred_succ(n,R)
    assert (a,b) not in R and (b,a) not in R
    assert pred[b] <= pred[a]
    D=pred[a]-pred[b]
    T={x for x in D if not any((x,y) in R for y in D)}
    S={z for z in range(n) if (b,z) in R and (z,a) not in R and (a,z) not in R}
    U={z for z in S if not any((y,z) in R for y in S)}
    return pred,succ,D,T,S,U

def check(name,n,rel,a,b,t,u,expected):
    R=closure(n,rel)
    assert R==set(rel), (name,"relation input not transitively closed")
    assert width(n,R)==3
    comp=R|{(y,x) for x,y in R}
    inc={(x,y) for x,y in combinations(range(n),2) if (x,y) not in comp}
    assert graph_connected(n,R)
    assert graph_connected(n,inc)
    pred,succ,D,T,S,U=canonical(n,R,a,b)
    assert t in T and u in U and (t,u) in R
    assert (t,a) in R and (b,u) in R
    assert all((x,y) not in R and (y,x) not in R
               for x,y in [(a,b),(b,t),(u,a)])
    exts=linear_extensions(n,R); E=len(exts)
    p=count_before(exts,a,b)
    A=count_before(exts,b,t)
    B=count_before(exts,u,a)
    I=sum(before(e,b,t) and before(e,u,a) for e in exts)
    det=I*E-A*B
    assert (E,p,A,B,I,det)==expected
    assert 3*p<E and 3*A<E and 3*B<E

    valid=[]
    for perm in permutations((t,a,b,u)):
        pos={x:i for i,x in enumerate(perm)}
        if pos[t]<pos[a] and pos[t]<pos[u] and pos[b]<pos[u]:
            valid.append(perm)
    assert len(valid)==5
    wc=defaultdict(int)
    for e in exts:
        wc[tuple(sorted((t,a,b,u),key=e.index))]+=1
    assert set(wc)==set(valid)
    w1=wc[(t,a,b,u)]
    w2=wc[(t,b,a,u)]
    w3=wc[(t,b,u,a)]
    w4=wc[(b,t,a,u)]
    w5=wc[(b,t,u,a)]
    assert p==w1
    assert A==w4+w5
    assert B==w3+w5
    assert I==w5
    assert det==w5*(w1+w2)-w3*w4

    balanced=[]
    for x,y in combinations(range(n),2):
        if (x,y) not in comp:
            c=count_before(exts,x,y)
            if E <= 3*c <= 2*E:
                balanced.append((x,y,c,E-c))
    assert balanced

    print(name)
    print("covers", covers(n,R))
    print("canonical", "a",a,"b",b,"D",sorted(D),"T",sorted(T),"S",sorted(S),"U",sorted(U),"t",t,"u",u)
    print("E",E,"endpoint",f"{p}/{E}","A",f"{A}/{E}","B",f"{B}/{E}","intersection",f"{I}/{E}")
    print("determinant",det)
    print("five_words", [w1,w2,w3,w4,w5])
    print("balanced_escape", balanced[0])
    print("comparability_connected",True,"incomparability_connected",True)
    return det

NEG_REL={
(0,2),(0,3),(0,6),(0,7),(0,8),
(1,3),
(2,6),(2,7),(2,8),
(4,1),(4,3),(4,5),(4,7),
(5,7),
(6,7),(6,8),
(8,7)
}
POS_REL={
(2,1),(2,3),(2,6),
(3,1),
(4,9),
(5,0),(5,1),(5,3),(5,7),(5,8),(5,9),
(6,1),(6,3),
(7,0),(7,8),(7,9),
(8,0)
}

dneg=check("NEGATIVE_SIGN",9,NEG_REL,3,5,0,7,(288,65,25,85,7,-109))
dpos=check("POSITIVE_SIGN",10,POS_REL,3,4,5,9,(2382,507,555,765,213,82791))
assert dneg<0<dpos
print("POS3_CROSS_GROUP_SIGN_INDETERMINACY_PASS")
