#!/usr/bin/env python3
"""PROB20-11 exact certificate: eliminate path4+edge K=4 classes 5 through 9.

Classes 5-6:
  parities 000111, edge distances (2,4,3,2), half bounds (1024,1027)
  parities 000111, edge distances (4,2,3,2), half bounds (1025,1026)
Classes 7-9:
  parities 001100, edge distances (2,3,2,2), half bounds (1027,1047)
  parities 001100, edge distances (2,3,2,4), half bounds (1025,1037)
  parities 001100, edge distances (4,3,2,2), half bounds (1024,1038)

All arithmetic/searches are exact in the 2048-point folded Hamming quotient.
No floating point, solver, timeout inference, or heuristic nonexistence claim.
"""
from itertools import combinations, product
from collections import Counter

N=2048

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

def parity(x): return x.bit_count()&1

def bits(S):
    z=0
    for i in S: z|=1<<i
    return z

def bit12(x,q): return ((x>>q)&1) if q<11 else 0

B0=[x for x in range(N) if fd(0,x)<=3]
assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0:m|=1<<(c^b)
    balls.append(m)
EVEN=0
for x in range(N):
    if parity(x)==0:EVEN|=1<<x
ALL=(1<<N)-1
ODD=ALL^EVEN

def tri_halves(a,b,c):
    z=balls[a]&balls[b]&balls[c]
    return ((z&EVEN).bit_count(),(z&ODD).bit_count())

trimax={}
for b in range(1,N):
    pb=parity(b); d0b=fd(0,b)
    for c in range(b+1,N):
        key=(0,pb,parity(c),d0b,fd(0,c),fd(b,c))
        h=tri_halves(0,b,c)
        old=trimax.get(key,(-1,-1))
        if h[0]>old[0] or h[1]>old[1]:
            trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

PERMS=((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))
def tri_max_for_centers(a,b,c):
    ps=(parity(a),parity(b),parity(c))
    D=((0,fd(a,b),fd(a,c)),(fd(a,b),0,fd(b,c)),(fd(a,c),fd(b,c),0))
    for q in PERMS:
        key=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        v=trimax.get(key)
        if v is not None:return v
    raise AssertionError((a,b,c,ps,D))

def active_def(cs):
    d0=d1=0
    for i,j,k in combinations(range(len(cs)),3):
        q=tri_halves(cs[i],cs[j],cs[k]);m=tri_max_for_centers(cs[i],cs[j],cs[k])
        d0+=m[0]-q[0];d1+=m[1]-q[1]
    return (d0,d1)

def triplet_signature(v3,v4,v5,blocks):
    ws=(v3,v4,v5);best=None
    for sw in (0,1):
        order=(0,2,1) if sw else (0,1,2)
        for flips in product((0,1),repeat=3):
            sig=[]
            for B in blocks:
                cnt=[0]*8
                for q in B:
                    pat=0
                    for t,r in enumerate(order):
                        z=bit12(ws[r],q)^flips[t]
                        if z:pat|=1<<t
                    cnt[pat]+=1
                sig.extend(cnt)
            sig=tuple(sig)
            if best is None or sig<best:best=sig
    return best

def four_sig(v2,v3,v4,v5,blocks):
    ws=(v2,v3,v4,v5);best=None
    for sw in (0,1):
        order=(0,1,3,2) if sw else (0,1,2,3)
        for flips in product((0,1),repeat=4):
            sig=[]
            for B in blocks:
                cnt=[0]*16
                for q in B:
                    pat=0
                    for t,r in enumerate(order):
                        z=bit12(ws[r],q)^flips[t]
                        if z:pat|=1<<t
                    cnt[pat]+=1
                sig.extend(cnt)
            tt=tuple(sig)
            if best is None or tt<best:best=tt
    return best

def candidate_list(active,budget,p):
    aset=set(active);out=[]
    for x in range(N):
        if x in aset or parity(x)!=p:continue
        if any(fd(x,a)!=(6 if p==parity(a) else 5) for a in active):continue
        d0=d1=0
        for i,j in combinations(range(len(active)),2):
            q=tri_halves(active[i],active[j],x);m=tri_max_for_centers(active[i],active[j],x)
            d0+=m[0]-q[0];d1+=m[1]-q[1]
        if d0<=budget[0] and d1<=budget[1]:out.append((x,(d0,d1)))
    return out

def search_isolates(active,budget,needE,needO):
    E=candidate_list(active,budget,0);O=candidate_list(active,budget,1);A=E+O;nE=len(E);n=len(A)
    adj=[0]*n;paircost={}
    for i in range(n):
        pi=0 if i<nE else 1
        for j in range(i+1,n):
            pj=0 if j<nE else 1
            if fd(A[i][0],A[j][0])!=(6 if pi==pj else 5):continue
            d0=d1=0
            for a in active:
                q=tri_halves(a,A[i][0],A[j][0]);m=tri_max_for_centers(a,A[i][0],A[j][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
            if d0<=budget[0] and d1<=budget[1]:
                adj[i]|=1<<j;adj[j]|=1<<i;paircost[(i,j)]=(d0,d1)
    sel=[];nodes=0
    def rec(mask,eleft,oleft,c0,c1):
        nonlocal nodes
        nodes+=1
        if c0>budget[0] or c1>budget[1]:return False
        if eleft==0 and oleft==0:return True
        if (mask&((1<<nE)-1)).bit_count()<eleft or (mask>>nE).bit_count()<oleft:return False
        qmask=mask
        while qmask:
            if qmask.bit_count()<eleft+oleft:return False
            l=qmask&-qmask;i=l.bit_length()-1;qmask-=l
            p=0 if i<nE else 1
            if (p==0 and eleft==0) or (p==1 and oleft==0):continue
            d0,d1=A[i][1];ok=True
            for j in sel:
                key=(j,i) if j<i else (i,j);z=paircost.get(key)
                if z is None:ok=False;break
                d0+=z[0];d1+=z[1]
            if not ok or c0+d0>budget[0] or c1+d1>budget[1]:continue
            for u,v in combinations(sel,2):
                q=tri_halves(A[u][0],A[v][0],A[i][0]);m=tri_max_for_centers(A[u][0],A[v][0],A[i][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
                if c0+d0>budget[0] or c1+d1>budget[1]:ok=False;break
            if not ok:continue
            sel.append(i)
            if rec(qmask&adj[i],eleft-(p==0),oleft-(p==1),c0+d0,c1+d1):return True
            sel.pop()
        return False
    found=rec((1<<n)-1,needE,needO,0,0)
    return found,(len(E),len(O),len(paircost),nodes)

def active_orbits_000111(base,budget,blocks):
    v0,v1,v2=base
    V3=[x for x in range(N) if parity(x)==1 and fd(x,v2)==3 and fd(x,v0)==5 and fd(x,v1)==5]
    OE=[x for x in range(N) if parity(x)==1 and fd(x,v0)==5 and fd(x,v1)==5 and fd(x,v2)==5]
    pairs=[(a,b) for a,b in combinations(OE,2) if fd(a,b)==2]
    configs=[]
    for v3 in V3:
        allowed={x for x in OE if fd(x,v3)==6}
        for v4,v5 in pairs:
            if v4 not in allowed or v5 not in allowed:continue
            d=active_def([v0,v1,v2,v3,v4,v5])
            if d[0]<=budget[0] and d[1]<=budget[1]:configs.append((v3,v4,v5,d))
    groups={}
    for v3,v4,v5,d in configs:
        groups.setdefault(triplet_signature(v3,v4,v5,blocks),[]).append((v3,v4,v5,d))
    return V3,OE,configs,groups

def active_groups_001100(v0,v1,v2,V3,Ebase,dedge,budget,blocks):
    pairs=[(a,b) for a,b in combinations(Ebase,2) if fd(a,b)==dedge]
    cfg=[]
    for v3 in V3:
        allowed={x for x in Ebase if fd(x,v3)==5}
        for a,b in pairs:
            if a not in allowed or b not in allowed:continue
            d=active_def([v0,v1,v2,v3,a,b])
            if d[0]<=budget[0] and d[1]<=budget[1]:cfg.append((v3,a,b,d))
    groups={}
    for v3,a,b,d in cfg:groups.setdefault(four_sig(v2,v3,a,b,blocks),[]).append((v3,a,b,d))
    return pairs,cfg,groups

# Class 5.
P=(0,bits([0,1]),bits([0,1,2,3,4,5]));B5=([0,1],[2,3,4,5],[6,7,8,9,10,11])
V3,OE,C,G=active_orbits_000111(P,(0,3),B5)
assert len(V3)==144 and len(OE)==520 and len(C)==13680
assert Counter(d for *_,d in C)==Counter({(0,0):13680})
assert sorted(map(len,G.values()))==[720,1440,1440,1440,4320,4320]
S5=[]
for arr in G.values():
    rep=arr[0][:3];found,stats=search_isolates(list(P)+list(rep),(0,3),3,3);assert not found;S5.append((len(arr),rep,stats))

# Class 6.
Q=(0,bits([0,1,2,3]),bits([0,1,2,3,4,5]));B6=([0,1,2,3],[4,5],[6,7,8,9,10,11])
V3b,OEb,Cb,Gb=active_orbits_000111(Q,(1,2),B6)
assert len(V3b)==96 and len(OEb)==520 and len(Cb)==13860
assert Counter(d for *_,d in Cb)==Counter({(0,0):13860})
assert sorted(map(len,Gb.values()))==[180,720,1440,1440,1440,8640]
S6=[]
for arr in Gb.values():
    rep=arr[0][:3];found,stats=search_isolates(list(Q)+list(rep),(1,2),3,3);assert not found;S6.append((len(arr),rep,stats))

# Classes 7-8 share normalized first three path centers.
R0=0;R1=bits([0,1]);R2=bits([0,1,2,3,4])
assert (fd(R0,R1),fd(R1,R2),fd(R0,R2))==(2,3,5)
R3=[x for x in range(N) if parity(x)==1 and fd(x,R2)==2 and fd(x,R0)==5 and fd(x,R1)==5]
RE=[x for x in range(N) if parity(x)==0 and fd(x,R0)==6 and fd(x,R1)==6 and fd(x,R2)==5]
assert len(R3)==35 and len(RE)==210
BR=([0,1],[2,3,4],[5,6,7,8,9,10,11])
P7,C7,G7=active_groups_001100(R0,R1,R2,R3,RE,2,(3,23),BR)
assert len(P7)==2415 and len(C7)==7770 and Counter(d for *_,d in C7)==Counter({(0,0):7770})
assert sorted(map(len,G7.values()))==[630,840,2520,3780]
S7=[]
for arr in G7.values():
    rep=arr[0][:3];found,stats=search_isolates([R0,R1,R2,*rep],(3,23),2,4);assert not found;S7.append((len(arr),rep,stats))
P8,C8,G8=active_groups_001100(R0,R1,R2,R3,RE,4,(1,13),BR)
assert len(P8)==10920 and len(C8)==20790 and Counter(d for *_,d in C8)==Counter({(0,0):20790})
assert sorted(map(len,G8.values()))==[1890,2520,3780,5040,7560]
S8=[]
for arr in G8.values():
    rep=arr[0][:3];found,stats=search_isolates([R0,R1,R2,*rep],(1,13),2,4);assert not found;S8.append((len(arr),rep,stats))

# Class 9.
T0=0;T1=bits([0,1,2,3]);T2=bits([0,1,2,4,5])
assert (fd(T0,T1),fd(T1,T2),fd(T0,T2))==(4,3,5)
T3=[x for x in range(N) if parity(x)==1 and fd(x,T2)==2 and fd(x,T0)==5 and fd(x,T1)==5]
TE=[x for x in range(N) if parity(x)==0 and fd(x,T0)==6 and fd(x,T1)==6 and fd(x,T2)==5]
assert len(T3)==33 and len(TE)==165
BT=([0,1,2],[3],[4,5],[6,7,8,9,10,11])
P9,C9,G9=active_groups_001100(T0,T1,T2,T3,TE,2,(0,14),BT)
assert len(P9)==1425 and len(C9)==5580 and Counter(d for *_,d in C9)==Counter({(0,0):5580})
assert sorted(map(len,G9.values()))==[180,180,180,360,360,1080,1080,2160]
S9=[]
for arr in G9.values():
    rep=arr[0][:3];found,stats=search_isolates([T0,T1,T2,*rep],(0,14),2,4);assert not found;S9.append((len(arr),rep,stats))

print('CERTIFICATE PASSED')
print('class5:',len(C),sorted(map(len,G.values())),sorted(S5))
print('class6:',len(Cb),sorted(map(len,Gb.values())),sorted(S6))
print('class7:',len(C7),sorted(map(len,G7.values())),sorted(S7))
print('class8:',len(C8),sorted(map(len,G8.values())),sorted(S8))
print('class9:',len(C9),sorted(map(len,G9.values())),sorted(S9))
print('CONCLUSION: path4+edge classes 5,6,7,8,9 are all impossible')