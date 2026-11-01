#!/usr/bin/env python3
"""PROB20-11 exact certificate: eliminate all four K=4 classes whose
close-edge graph is a 3-star plus a disjoint edge.

No solver, no floating point. All computations occur in the 2048-point
folded Hamming quotient F_2^12/<1> and use exact integer bitsets.
"""
from itertools import combinations
from collections import Counter

N=2048
MASK12=(1<<12)-1

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

def bits(S):
    z=0
    for i in S:z|=1<<i
    return z

def canon12(x):
    return x if x.bit_count()<=6 else x^MASK12

B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0:m|=1<<(c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if x.bit_count()%2==0:EVEN|=1<<x
ODD=((1<<N)-1)^EVEN

def tri_halves(a,b,c):
    z=balls[a]&balls[b]&balls[c]
    return ((z&EVEN).bit_count(),(z&ODD).bit_count())

tri_max={}
for a in range(1,N):
    da=fd(0,a)
    for b in range(a+1,N):
        key=(da,fd(0,b),fd(a,b))
        t=tri_halves(0,a,b)
        old=tri_max.get(key)
        if old is None:tri_max[key]=t
        else:tri_max[key]=(max(old[0],t[0]),max(old[1],t[1]))

def coarse_tri_max(a,b,c):
    key=(fd(a,b),fd(a,c),fd(b,c))
    v=tri_max.get(key)
    if v is None:v=tri_max[(key[1],key[0],key[2])]
    return v if a.bit_count()%2==0 else (v[1],v[0])

def active_def(cs):
    d=[0,0]
    for i,j,k in combinations(range(len(cs)),3):
        a=tri_halves(cs[i],cs[j],cs[k]);m=coarse_tri_max(cs[i],cs[j],cs[k])
        d[0]+=m[0]-a[0];d[1]+=m[1]-a[1]
    return tuple(d)

def search_isolates(active,budget,needE,needO,all_completions=False):
    cand={0:[],1:[]}
    for p in (0,1):
        for x in range(N):
            if x in active or x.bit_count()%2!=p:continue
            if any(fd(x,a)!=(6 if p==a.bit_count()%2 else 5) for a in active):continue
            d=[0,0]
            for i,j in combinations(range(len(active)),2):
                q=tri_halves(active[i],active[j],x);m=coarse_tri_max(active[i],active[j],x)
                d[0]+=m[0]-q[0];d[1]+=m[1]-q[1]
            if d[0]<=budget[0] and d[1]<=budget[1]:cand[p].append((x,tuple(d)))
    E,O=cand[0],cand[1];A=E+O;nE=len(E)
    adj=[0]*len(A);pc={}
    for i in range(len(A)):
        pi=0 if i<nE else 1
        for j in range(i+1,len(A)):
            pj=0 if j<nE else 1
            if fd(A[i][0],A[j][0])!=(6 if pi==pj else 5):continue
            d=[0,0]
            for a in active:
                q=tri_halves(a,A[i][0],A[j][0]);m=coarse_tri_max(a,A[i][0],A[j][0])
                d[0]+=m[0]-q[0];d[1]+=m[1]-q[1]
            if d[0]<=budget[0] and d[1]<=budget[1]:
                adj[i]|=1<<j;adj[j]|=1<<i;pc[(i,j)]=tuple(d)
    sel=[];nodes=0;solutions=[]
    def rec(mask,eleft,oleft,c0,c1):
        nonlocal nodes
        nodes+=1
        if c0>budget[0] or c1>budget[1]:return False
        if eleft==0 and oleft==0:
            solutions.append(tuple(sel));return not all_completions
        if (mask&((1<<nE)-1)).bit_count()<eleft or (mask>>nE).bit_count()<oleft:return False
        q=mask
        while q:
            l=q&-q;i=l.bit_length()-1;q-=l
            p=0 if i<nE else 1
            if p==0 and eleft==0:continue
            if p==1 and oleft==0:continue
            d0,d1=A[i][1];ok=True
            for j in sel:
                key=(j,i) if j<i else (i,j)
                if key not in pc:ok=False;break
                r=pc[key];d0+=r[0];d1+=r[1]
            if not ok or c0+d0>budget[0] or c1+d1>budget[1]:continue
            for aa in range(len(sel)):
                for bb in range(aa+1,len(sel)):
                    j,k=sel[aa],sel[bb]
                    qh=tri_halves(A[j][0],A[k][0],A[i][0]);mh=coarse_tri_max(A[j][0],A[k][0],A[i][0])
                    d0+=mh[0]-qh[0];d1+=mh[1]-qh[1]
                    if c0+d0>budget[0] or c1+d1>budget[1]:ok=False;break
                if not ok:break
            if not ok:continue
            sel.append(i)
            stop=rec(q&adj[i],eleft-(p==0),oleft-(p==1),c0+d0,c1+d1)
            sel.pop()
            if stop:return True
        return False
    found=rec((1<<len(A))-1,needE,needO,0,0)
    return found,{"nE":len(E),"nO":len(O),"pairs":len(pc),"nodes":nodes,"A":A},solutions

# mixed star, same-parity arms 4,4
S0=0;S1=bits([0,1,2,3]);S2=bits([0,4,5,6])
S3=[x for x in range(N) if x.bit_count()%2==1 and fd(x,S0)==3 and fd(x,S1)==5 and fd(x,S2)==5]
Ostar=[x for x in range(N) if x.bit_count()%2==1 and fd(x,S0)==5 and fd(x,S1)==5 and fd(x,S2)==5]
active=[]
for v3 in S3:
    C=[x for x in Ostar if fd(x,v3)==6]
    for i,j in combinations(range(len(C)),2):
        if fd(C[i],C[j])==2:
            cs=[S0,S1,S2,v3,C[i],C[j]]
            if active_def(cs)==(0,0):active.append((v3,C[i],C[j]))
assert len(active)==7200
blocks=[[0],[1,2,3],[4,5,6],[7,8,9,10,11]]
def sig_m44(v3,v4,v5):
    M=[canon12(v3),canon12(v4),canon12(v5)];out=[]
    for swleaf in (0,1):
        bl=[blocks[0],blocks[2],blocks[1],blocks[3]] if swleaf else blocks
        for swedge in (0,1):
            order=(0,2,1) if swedge else (0,1,2);s=[]
            for B in bl:
                c=[0]*8
                for q in B:
                    p=0
                    for t,r in enumerate(order):
                        if (M[r]>>q)&1:p|=1<<t
                    c[p]+=1
                s+=c
            out.append(tuple(s))
    return min(out)
orbits={}
for r in active:orbits.setdefault(sig_m44(*r),r)
assert len(orbits)==10
struct=0;maxunion=0
for r in orbits.values():
    cs=[S0,S1,S2,*r]
    found,st,sol=search_isolates(cs,(0,0),3,3,all_completions=True)
    for ss in sol:
        struct+=1
        U=0
        for c in cs+[st['A'][i][0] for i in ss]:U|=balls[c]
        maxunion=max(maxunion,U.bit_count())
assert struct==2 and maxunion==1969

# mixed star, same-parity arms 2,4
M0=0;M1=bits([0,1]);M2=bits([2,3,4,5])
M3=[x for x in range(N) if x.bit_count()%2==1 and fd(x,M0)==3 and fd(x,M1)==5 and fd(x,M2)==5]
MO=[x for x in range(N) if x.bit_count()%2==1 and fd(x,M0)==5 and fd(x,M1)==5 and fd(x,M2)==5]
active=[]
for v3 in M3:
    C=[x for x in MO if fd(x,v3)==6]
    for i,j in combinations(range(len(C)),2):
        if fd(C[i],C[j])==2:
            cs=[M0,M1,M2,v3,C[i],C[j]]
            if active_def(cs)==(0,0):active.append((v3,C[i],C[j]))
assert len(active)==17640
blocksM=[[0,1],[2,3,4,5],[6,7,8,9,10,11]]
def sig_m24(v3,v4,v5):
    M=[canon12(v3),canon12(v4),canon12(v5)];out=[]
    for sw in (0,1):
        order=(0,2,1) if sw else (0,1,2);s=[]
        for B in blocksM:
            c=[0]*8
            for q in B:
                p=0
                for t,r in enumerate(order):
                    if (M[r]>>q)&1:p|=1<<t
                c[p]+=1
            s+=c
        out.append(tuple(s))
    return min(out)
orbits={}
for r in active:orbits.setdefault(sig_m24(*r),r)
assert len(orbits)==7
for r in orbits.values():
    cs=[M0,M1,M2,*r]
    found,st,sol=search_isolates(cs,(3,3),3,3)
    assert not found

# same-parity star arm multiset {2,4,4}
Q=[0,bits([0,1]),bits([2,3,4,5]),bits([2,6,7,8])]
QO=[x for x in range(N) if x.bit_count()%2==1 and all(fd(x,e)==5 for e in Q)]
pairs=[]
for i,j in combinations(range(len(QO)),2):
    if fd(QO[i],QO[j])==2:
        d=active_def(Q+[QO[i],QO[j]])
        if d[0]<=4 and d[1]<=10:pairs.append((QO[i],QO[j],d))
assert len(QO)==395 and Counter(d for _,_,d in pairs)==Counter({(2,6):468,(0,0):234})
blocksQ=[[0,1],[2],[3,4,5],[6,7,8],[9,10,11]]
def sig_q(a,b):
    M=[canon12(a),canon12(b)];out=[]
    for swleaf in (0,1):
        bl=[blocksQ[0],blocksQ[1],blocksQ[3],blocksQ[2],blocksQ[4]] if swleaf else blocksQ
        for swedge in (0,1):
            order=(1,0) if swedge else (0,1);s=[]
            for B in bl:
                c=[0]*4
                for q in B:
                    p=0
                    for t,r in enumerate(order):
                        if (M[r]>>q)&1:p|=1<<t
                    c[p]+=1
                s+=c
            out.append(tuple(s))
    return min(out)
orbits={}
for a,b,d in pairs:orbits.setdefault((d,sig_q(a,b)),(a,b,d))
assert len(orbits)==12
for a,b,d in orbits.values():
    found,st,sol=search_isolates(Q+[a,b],(4-d[0],10-d[1]),2,4)
    assert not found

# same-parity star arm multiset {4,4,4}; two star-isometry types
Rstars=[
 [0,bits([0,1,2,3]),bits([0,4,5,6]),bits([0,7,8,9])],
 [0,bits([0,1,2,3]),bits([0,4,5,6]),bits([1,4,7,8])],
]
total_edges=0
for R in Rstars:
    RO=[x for x in range(N) if x.bit_count()%2==1 and all(fd(x,e)==5 for e in R)]
    assert len(RO)==351
    P=[]
    for i,j in combinations(range(len(RO)),2):
        if fd(RO[i],RO[j])==2:
            d=active_def(R+[RO[i],RO[j]])
            if d[0]<=2 and d[1]<=12:P.append((RO[i],RO[j],d))
    total_edges+=len(P)
    for a,b,d in P:
        found,st,sol=search_isolates(R+[a,b],(2-d[0],12-d[1]),2,4)
        assert not found
assert total_edges==864

print('CERTIFICATE PASSED')
print('mixed 4,4: 10 active orbits, 2 structural completions, max union 1969')
print('mixed 2,4: 7 active orbits, no isolate completion')
print('same-parity {2,4,4}: 12 active orbits, no completion')
print('same-parity {4,4,4}: all 864 normalized active edges exhausted, no completion')
print('CONCLUSION: all four 3-star + disjoint-edge K=4 canonical classes are impossible')
