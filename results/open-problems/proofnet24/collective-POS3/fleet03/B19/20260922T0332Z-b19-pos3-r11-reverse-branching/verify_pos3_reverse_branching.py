#!/usr/bin/env python3
from itertools import combinations

COVERS=[(0,3),(1,2),(1,3),(2,4),(2,5),(3,5)]
N=6
A,B,D,U=3,2,0,4

def closure(n,covers):
    R=[[False]*n for _ in range(n)]
    for x,y in covers:R[x][y]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:R[i][j]=True
    return R

def extensions(R):
    n=len(R)
    pred=[{u for u in range(n) if R[u][v]} for v in range(n)]
    out=[]
    def rec(word,rem):
        if not rem:
            out.append(tuple(word));return
        used=set(word)
        for v in sorted(rem):
            if pred[v] <= used:
                rec(word+[v],rem-{v})
    rec([],set(range(n)))
    return out

def width(R):
    n=len(R);w=0
    for mask in range(1<<n):
        V=[i for i in range(n) if (mask>>i)&1]
        if len(V)<=w:continue
        if all(not R[x][y] and not R[y][x] for x,y in combinations(V,2)):
            w=len(V)
    return w

def pair_count(ext,u,v):
    return sum(L.index(u)<L.index(v) for L in ext)

def pred(R,v):
    return {u for u in range(len(R)) if R[u][v]}

def min_succ_blockers(R,base,other):
    inc=lambda x,y:not R[x][y] and not R[y][x] and x!=y
    cand=[z for z in range(len(R)) if R[base][z] and inc(z,other)]
    return [z for z in cand if not any(w!=z and w in cand and R[w][z] for w in cand)]

def reverse_nonneutral(ext,R,a,b):
    total=0
    for L in ext:
        pa,pb=L.index(a),L.index(b)
        if pb>pa:continue
        mid=L[pb+1:pa]
        if any(R[z][a] or R[a][z] or R[z][b] or R[b][z] for z in mid):
            total+=1
    return total

R=closure(N,COVERS)
Elist=extensions(R); E=len(Elist)
assert E==14
assert width(R)==2
assert pred(R,B)=={1}
assert pred(R,A)=={0,1}
assert pred(R,A)-pred(R,B)=={D}
assert min_succ_blockers(R,B,A)==[U]

pab=pair_count(Elist,A,B)
pbd=pair_count(Elist,B,D)
pua=pair_count(Elist,U,A)
assert (pab,pbd,pua)==(4,4,4)
assert 3*pab<E and 3*pbd<E and 3*pua<E

# Here M_a(b) is empty, so Q=E in the endpoint identity.
M=min_succ_blockers(R,A,B)
assert M==[]
Q=E
Rrem=reverse_nonneutral(Elist,R,A,B)
assert Rrem==6
assert 2*(E-pab)==Q+Rrem

EA={L for L in Elist if L.index(B)<L.index(D)}
EB={L for L in Elist if L.index(U)<L.index(A)}
assert len(EA)==4 and len(EB)==4
assert len(EA & EB)==2
assert len(EA | EB)==6==Rrem
assert 3*len(EA)<E and 3*len(EB)<E and 3*len(EA|EB)>E
assert len(EA-EB)==2 and len(EB-EA)==2

balanced=[]
for x,y in combinations(range(N),2):
    if R[x][y] or R[y][x]:continue
    c=pair_count(Elist,x,y)
    if E <= 3*c <= 2*E:
        balanced.append((x,y,c,E-c))
assert balanced==[(0,1,5,9),(4,5,9,5)]
assert all(A not in p[:2] and B not in p[:2] for p in balanced)

print('E=',E)
print('WIDTH=',width(R))
print('STRICT_ENDPOINT a,b=',(A,B),'P(a<b)=',f'{pab}/{E}')
print('D_TOP=',D,'P(b<d)=',f'{pbd}/{E}')
print('U_MIN=',U,'P(u<a)=',f'{pua}/{E}')
print('Q=',Q,'R=',Rrem,'Q+R=',Q+Rrem)
print('REVERSE_CHANNEL_A=',len(EA),'REVERSE_CHANNEL_B=',len(EB),'INTERSECTION=',len(EA&EB),'UNION=',len(EA|EB))
print('EXCLUSIVE_A=',len(EA-EB),'EXCLUSIVE_B=',len(EB-EA))
print('BALANCED_PAIRS=',balanced)
print('POS3_B19_REVERSE_BRANCHING_CERTIFICATE_PASS')
