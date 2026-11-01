#!/usr/bin/env python3
"""PROB20-11 exact certificate: eliminate the final four K=4 P4+K2 classes.

Usage:
  python 2026-09-15T175741Z__path4_edge_final4_certificate.py 1
  python ... 2
  python ... 3
  python ... 4

Each mode is an independent exact finite computation in the 2048-point folded
Hamming quotient. No floating point, MILP, heuristic, or timeout inference.
"""
import sys
from itertools import combinations, product

N=2048
def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)
def parity(x): return x.bit_count()&1
def bits(S):
    z=0
    for i in S:z|=1<<i
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

# Exact maximum triple intersections for every realizable parity/distance type.
trimax={}
for b in range(1,N):
    pb=parity(b); db=fd(0,b)
    for c in range(b+1,N):
        key=(0,pb,parity(c),db,fd(0,c),fd(b,c))
        h=tri_halves(0,b,c)
        old=trimax.get(key,(-1,-1))
        if h[0]>old[0] or h[1]>old[1]:
            trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

PERMS=((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))
def tri_max(a,b,c):
    ps=(parity(a),parity(b),parity(c))
    D=((0,fd(a,b),fd(a,c)),(fd(a,b),0,fd(b,c)),(fd(a,c),fd(b,c),0))
    for q in PERMS:
        v=trimax.get((ps[q[0]],ps[q[1]],ps[q[2]],
                      D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]]))
        if v is not None:return v
    raise AssertionError((a,b,c,ps,D))

def active_def(cs):
    d0=d1=0
    for i,j,k in combinations(range(len(cs)),3):
        q=tri_halves(cs[i],cs[j],cs[k]);m=tri_max(cs[i],cs[j],cs[k])
        d0+=m[0]-q[0];d1+=m[1]-q[1]
    return (d0,d1)

def sig3(ws,blocks):
    """Complete orbit signature under within-block coordinate permutations,
    independent antipodal representative flips, and swapping odd-edge endpoints.
    """
    best=None
    for sw in (0,1):
        order=(0,2,1) if sw else (0,1,2)
        for flips in product((0,1),repeat=3):
            out=[]
            for B in blocks:
                cnt=[0]*8
                for q in B:
                    pat=0
                    for t,r in enumerate(order):
                        if bit12(ws[r],q)^flips[t]:pat|=1<<t
                    cnt[pat]+=1
                out.extend(cnt)
            out=tuple(out)
            if best is None or out<best:best=out
    return best

def candidate_list(active,budget,p):
    aset=set(active);out=[]
    for x in range(N):
        if x in aset or parity(x)!=p:continue
        if any(fd(x,a)!=(6 if p==parity(a) else 5) for a in active):continue
        d0=d1=0
        for i,j in combinations(range(len(active)),2):
            q=tri_halves(active[i],active[j],x);m=tri_max(active[i],active[j],x)
            d0+=m[0]-q[0];d1+=m[1]-q[1]
        if d0<=budget[0] and d1<=budget[1]:
            out.append((x,(d0,d1)))
    return out

def search_cover(active,budget,needE=2,needO=4):
    """Exhaust all isolate completions surviving exact triple-deficit budget.
    At every leaf compute the actual 12-ball union. Return whether any leaf covers.
    """
    E=candidate_list(active,budget,0);O=candidate_list(active,budget,1)
    A=E+O;nE=len(E);n=len(A)
    adj=[0]*n;paircost={}
    for i in range(n):
        pi=0 if i<nE else 1
        for j in range(i+1,n):
            pj=0 if j<nE else 1
            if fd(A[i][0],A[j][0])!=(6 if pi==pj else 5):continue
            d0=d1=0
            for a in active:
                q=tri_halves(a,A[i][0],A[j][0]);m=tri_max(a,A[i][0],A[j][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
            if d0<=budget[0] and d1<=budget[1]:
                adj[i]|=1<<j;adj[j]|=1<<i;paircost[(i,j)]=(d0,d1)
    baseu=0
    for c in active:baseu|=balls[c]
    sel=[];nodes=0;leaves=0;maxu=baseu.bit_count();best=None
    def rec(mask,eleft,oleft,c0,c1,u):
        nonlocal nodes,leaves,maxu,best
        nodes+=1
        if c0>budget[0] or c1>budget[1]:return False
        if eleft==0 and oleft==0:
            leaves+=1
            uc=u.bit_count()
            if uc>maxu:
                maxu=uc;best=[A[i][0] for i in sel]
            return uc==N
        if (mask&((1<<nE)-1)).bit_count()<eleft or (mask>>nE).bit_count()<oleft:return False
        qmask=mask
        while qmask:
            if qmask.bit_count()<eleft+oleft:return False
            l=qmask&-qmask;i=l.bit_length()-1;qmask-=l
            p=0 if i<nE else 1
            if (p==0 and eleft==0) or (p==1 and oleft==0):continue
            d0,d1=A[i][1];ok=True
            for j in sel:
                z=paircost.get((j,i) if j<i else (i,j))
                if z is None:ok=False;break
                d0+=z[0];d1+=z[1]
            if not ok or c0+d0>budget[0] or c1+d1>budget[1]:continue
            for u0,v0 in combinations(sel,2):
                q=tri_halves(A[u0][0],A[v0][0],A[i][0]);m=tri_max(A[u0][0],A[v0][0],A[i][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
                if c0+d0>budget[0] or c1+d1>budget[1]:ok=False;break
            if not ok:continue
            sel.append(i)
            if rec(qmask&adj[i],eleft-(p==0),oleft-(p==1),c0+d0,c1+d1,u|balls[A[i][0]]):
                return True
            sel.pop()
        return False
    found=rec((1<<n)-1,needE,needO,0,0,baseu)
    return found,(len(E),len(O),len(paircost),nodes,leaves,maxu,best)

def run_case(case):
    if case==1:
        base=(0,bits([0,1]),bits([0,1,2,3,4,5]))
        d23=2;budget=(6,22);blocks=([0,1],[2,3,4,5],[6,7,8,9,10,11])
        expected=(12,520,11000,9360,8)
        expected_orbits=[720,720,720,720,1440,1440,1440,2160]
        expected_leaves=0;expected_maxu=None
    elif case==2:
        base=(0,bits([0,1]),bits([0,1,2,3,4,5]))
        d23=4;budget=(4,18);blocks=([0,1],[2,3,4,5],[6,7,8,9,10,11])
        expected=(120,520,11000,88200,30)
        expected_orbits=[360,720,720,720,1440,1440,1440,1440,1440,2160,2160,2160,2160,2160,2160,2160,2880,2880,2880,2880,4320,4320,4320,4320,4320,4320,4320,4320,8640,8640]
        expected_leaves=2;expected_maxu=1966
    elif case==3:
        base=(0,bits([0,1,2,3]),bits([0,1,2,3,4,5]))
        d23=4;budget=(4,12);blocks=([0,1,2,3],[4,5],[6,7,8,9,10,11])
        expected=(90,520,11000,79110,29)
        expected_orbits=[90,540,720,720,720,720,720,720,2160,2160,2160,2160,2160,2160,2160,2160,2160,2160,2160,2160,2160,2880,2880,2880,2880,8640,8640,8640,8640]
        expected_leaves=0;expected_maxu=None
    elif case==4:
        base=(0,bits([0,1,2,3]),bits([0,1,2,4,5,6]))
        d23=4;budget=(2,14);blocks=([0,1,2],[3],[4,5,6],[7,8,9,10,11])
        expected=(105,470,9415,41670,74)
        expected_orbits=None
        expected_leaves=0;expected_maxu=None
    else:
        raise SystemExit("case must be 1,2,3,4")

    v0,v1,v2=base
    assert fd(v0,v2)==6
    V3=[x for x in range(N) if parity(x)==0 and fd(x,v2)==d23 and fd(x,v0)==6 and fd(x,v1)==6]
    O=[x for x in range(N) if parity(x)==1 and fd(x,v0)==fd(x,v1)==fd(x,v2)==5]
    pairs=[(a,b) for a,b in combinations(O,2) if fd(a,b)==2]
    cfg=[]
    for v3 in V3:
        allowed={x for x in O if fd(x,v3)==5}
        for a,b in pairs:
            if a not in allowed or b not in allowed:continue
            d=active_def([v0,v1,v2,v3,a,b])
            if d[0]<=budget[0] and d[1]<=budget[1]:
                cfg.append((v3,a,b,d))
    groups={}
    for v3,a,b,d in cfg:
        groups.setdefault(sig3((v3,a,b),blocks),[]).append((v3,a,b,d))
    got=(len(V3),len(O),len(pairs),len(cfg),len(groups))
    assert got==expected,(case,got,expected)
    if expected_orbits is not None:
        assert sorted(map(len,groups.values()))==expected_orbits

    total_leaves=0;max_union=0;positive=[]
    for arr in groups.values():
        rep=arr[0]
        found,st=search_cover([v0,v1,v2,rep[0],rep[1],rep[2]],budget)
        assert not found,(case,rep,st)
        total_leaves+=st[4]
        max_union=max(max_union,st[5])
        if st[4]:
            positive.append((len(arr),rep[:3],rep[3],st))
    assert total_leaves==expected_leaves,(case,total_leaves)
    if expected_maxu is not None:
        assert max_union==expected_maxu,(case,max_union)
    print("CASE",case,"PASSED")
    print("active counts V3/O/pairs/configs/orbits =",got)
    print("orbit sizes =",sorted(map(len,groups.values())))
    print("total relaxed isolate leaves =",total_leaves)
    print("maximum actual 12-ball union at a relaxed leaf =",max_union if total_leaves else "no leaf")
    if positive: print("positive-leaf orbits =",positive)
    print("CONCLUSION: no cover in class",case)

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit(__doc__)
    run_case(int(sys.argv[1]))
