from itertools import permutations
from fractions import Fraction

V = ("c",0,1,2,3,4,5)
covers = ((0,2),(0,4),(1,2),(2,3),("c",0))

def closure(V,covers):
    idx={v:i for i,v in enumerate(V)}
    n=len(V); lt=[[False]*n for _ in range(n)]
    for a,b in covers: lt[idx[a]][idx[b]]=True
    for k in range(n):
        for i in range(n):
            if lt[i][k]:
                for j in range(n):
                    if lt[k][j]: lt[i][j]=True
    return idx,lt

def linear_extensions(V,covers):
    idx,lt=closure(V,covers)
    out=[]
    for p in permutations(V):
        pos={v:i for i,v in enumerate(p)}
        if all(not lt[i][j] or pos[V[i]]<pos[V[j]]
               for i in range(len(V)) for j in range(len(V))):
            out.append(p)
    return out,idx,lt

def induced_count(W, V, idx, lt):
    W=tuple(W)
    if not W: return 1
    ans=0
    for p in permutations(W):
        pos={v:i for i,v in enumerate(p)}
        if all(not lt[idx[a]][idx[b]] or pos[a]<pos[b] for a in W for b in W):
            ans+=1
    return ans

LP,idxP,ltP=linear_extensions(V,covers)
Q=(0,1,2,3,4,5)
coversQ=((0,2),(0,4),(1,2),(2,3))
LQ,idxQ,ltQ=linear_extensions(Q,coversQ)
assert len(LP)==70 and len(LQ)==42

S={1,5}
for z in S:
    for t in Q:
        if ltQ[idxQ[t]][idxQ[z]]:
            assert t in S

def width(W, idx,lt):
    W=list(W); best=0
    for mask in range(1<<len(W)):
        A=[W[i] for i in range(len(W)) if mask>>i&1]
        if all(not lt[idx[a]][idx[b]] and not lt[idx[b]][idx[a]]
               for i,a in enumerate(A) for b in A[i+1:]):
            best=max(best,len(A))
    return best

assert width(S,idxQ,ltQ)==2
assert width(V,idxP,ltP)==3

ideals=[]
SS=list(S)
for mask in range(1<<len(S)):
    I={SS[i] for i in range(len(SS)) if mask>>i&1}
    if all(not ltQ[idxQ[t]][idxQ[z]] or t in I for z in I for t in S):
        ideals.append(frozenset(I))

obs={I:0 for I in ideals}
for p in LP:
    I=frozenset(z for z in S if p.index(z)<p.index("c"))
    obs[I]+=1
pred={}
for I in ideals:
    pred[I]=induced_count(I,Q,idxQ,ltQ)*induced_count(set(Q)-set(I),Q,idxQ,ltQ)
assert obs==pred
assert sum(pred.values())==len(LP)

def prob(L,a,b):
    return Fraction(sum(p.index(a)<p.index(b) for p in L),len(L))

assert prob(LP,"c",1)==Fraction(7,10)
assert prob(LP,"c",5)==Fraction(57,70)
assert prob(LP,1,5)==Fraction(24,35)
assert prob(LQ,1,5)==Fraction(5,7)

num=0
for I,w in pred.items():
    I=set(I); J=set(Q)-I
    if 1 in I and 5 not in I:
        num += w
    elif 5 in I and 1 not in I:
        pass
    elif 1 in I and 5 in I:
        LI=[p for p in permutations(tuple(I))
            if all(not ltQ[idxQ[a]][idxQ[b]] or p.index(a)<p.index(b) for a in I for b in I)]
        n=sum(p.index(1)<p.index(5) for p in LI)
        num += induced_count(J,Q,idxQ,ltQ)*n
    else:
        LJ=[p for p in permutations(tuple(J))
            if all(not ltQ[idxQ[a]][idxQ[b]] or p.index(a)<p.index(b) for a in J for b in J)]
        n=sum(p.index(1)<p.index(5) for p in LJ)
        num += induced_count(I,Q,idxQ,ltQ)*n
assert Fraction(num,len(LP))==Fraction(24,35)

print("POS3_IDEAL_CUT_RECURRENCE_CHECK_PASS")
print("eQ=42 eP=70 widthP=3 widthS=2")
print("cut_weights=" + repr(sorted((tuple(sorted(I)),w) for I,w in pred.items())))
print("Pr_P(c<1)=7/10 Pr_P(c<5)=57/70")
print("Pr_Q(1<5)=5/7 Pr_P(1<5)=24/35")
