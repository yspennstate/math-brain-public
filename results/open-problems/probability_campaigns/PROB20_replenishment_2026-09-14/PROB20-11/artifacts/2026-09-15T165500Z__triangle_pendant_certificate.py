#!/usr/bin/env python3
"""PROB20-11 exact certificate, 2026-09-15.

Standard-library-only exact finite verification in the folded Hamming quotient.
It exactly eliminates all six K=4 canonical classes whose close-edge graph
is a triangle with one pendant edge.

No floating point, solver, timeout inference, or heuristic witness is used.
"""
from itertools import combinations, product, permutations
from collections import defaultdict

N=2048

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

def parity(x): return x.bit_count()&1

def bits(S):
    z=0
    for i in S:z|=1<<i
    return z

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

def halves(m): return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pair_halves(a,b): return halves(balls[a]&balls[b])
def tri_halves(a,b,c): return halves(balls[a]&balls[b]&balls[c])

pairtbl={}
for p0 in (0,1):
    a=0 if p0==0 else 1
    for p1 in (0,1):
        seen=defaultdict(set)
        for b in range(N):
            if b==a or parity(b)!=p1:continue
            seen[fd(a,b)].add(pair_halves(a,b))
        for d,s in seen.items():
            assert len(s)==1
            pairtbl[(p0,p1,d)]=next(iter(s))

trimax={}
for b in range(1,N):
    for c in range(b+1,N):
        key=(0,parity(b),parity(c),fd(0,b),fd(0,c),fd(b,c))
        h=tri_halves(0,b,c)
        old=trimax.get(key,(-1,-1))
        trimax[key]=(max(old[0],h[0]),max(old[1],h[1]))
for key,h in list(trimax.items()):
    p0,p1,p2,d01,d02,d12=key
    trimax[(1,1-p1,1-p2,d01,d02,d12)]=(h[1],h[0])

def tri_max_for(p0,p1,p2,d01,d02,d12):
    ps=[p0,p1,p2]
    D=((0,d01,d02),(d01,0,d12),(d02,d12,0))
    for q in permutations(range(3)):
        key=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if key in trimax:return trimax[key]
    return None

def coarse_tri_max(a,b,c):
    return tri_max_for(parity(a),parity(b),parity(c),fd(a,b),fd(a,c),fd(b,c))

def active_def(cs):
    d0=d1=0
    for i,j,k in combinations(range(len(cs)),3):
        q=tri_halves(cs[i],cs[j],cs[k]);m=coarse_tri_max(cs[i],cs[j],cs[k])
        d0+=m[0]-q[0];d1+=m[1]-q[1]
    return (d0,d1)

def block_partition(words):
    d=defaultdict(list)
    for q in range(12):
        pat=tuple(((w>>q)&1) if q<11 else 0 for w in words)
        d[pat].append(q)
    return [d[k] for k in sorted(d)]

def sig_word(x,blocks):
    c=tuple(sum(((x>>q)&1) if q<11 else 0 for q in B) for B in blocks)
    s=tuple(map(len,blocks));cc=tuple(z-y for z,y in zip(s,c))
    return min(c,cc)

def pair_sig(x,y,blocks):
    best=None
    for fx,fy,sw in product((0,1),(0,1),(0,1)):
        v=[]
        for B in blocks:
            c=[0]*4
            for q in B:
                a=((x>>q)&1) if q<11 else 0;b=((y>>q)&1) if q<11 else 0
                if fx:a^=1
                if fy:b^=1
                if sw:a,b=b,a
                c[a+2*b]+=1
            v+=c
        t=tuple(v)
        if best is None or t<best:best=t
    return best

def tuple_sig(ws,blocks):
    m=len(ws)
    raw=[]
    for B in blocks:
        c=[0]*(1<<m)
        for pos in B:
            pat=0
            for r,w in enumerate(ws):
                b=((w>>pos)&1) if pos<11 else 0
                if b:pat|=1<<r
            c[pat]+=1
        raw.append(c)
    best=None
    for q in permutations(range(m)):
        for flips in product((0,1),repeat=m):
            v=[]
            for c in raw:
                cc=[0]*(1<<m)
                for pat,count in enumerate(c):
                    if not count:continue
                    npat=0
                    for t,r in enumerate(q):
                        bit=(pat>>r)&1
                        if flips[t]:bit^=1
                        if bit:npat|=1<<t
                    cc[npat]+=count
                v.extend(cc)
            z=tuple(v)
            if best is None or z<best:best=z
    return best

def candidates(active,budget,p):
    out=[];aset=set(active)
    for x in range(N):
        if x in aset or parity(x)!=p:continue
        if any(fd(x,a)!=(6 if p==parity(a) else 5) for a in active):continue
        d0=d1=0
        for i,j in combinations(range(len(active)),2):
            q=tri_halves(active[i],active[j],x);m=coarse_tri_max(active[i],active[j],x)
            d0+=m[0]-q[0];d1+=m[1]-q[1]
        if d0<=budget[0] and d1<=budget[1]:out.append((x,(d0,d1)))
    return out

def search_completion(active,budget,needE,needO):
    E=candidates(active,budget,0);O=candidates(active,budget,1);A=E+O;nE=len(E);n=len(A)
    adj=[0]*n;pc={}
    for i in range(n):
        pi=0 if i<nE else 1
        for j in range(i+1,n):
            pj=0 if j<nE else 1
            if fd(A[i][0],A[j][0])!=(6 if pi==pj else 5):continue
            d0=d1=0
            for a in active:
                q=tri_halves(a,A[i][0],A[j][0]);m=coarse_tri_max(a,A[i][0],A[j][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
            if d0<=budget[0] and d1<=budget[1]:
                adj[i]|=1<<j;adj[j]|=1<<i;pc[(i,j)]=(d0,d1)
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
                key=(j,i) if j<i else (i,j)
                if key not in pc:ok=False;break
                z=pc[key];d0+=z[0];d1+=z[1]
            if not ok or c0+d0>budget[0] or c1+d1>budget[1]:continue
            for u,v in combinations(sel,2):
                q=tri_halves(A[u][0],A[v][0],A[i][0]);m=coarse_tri_max(A[u][0],A[v][0],A[i][0])
                d0+=m[0]-q[0];d1+=m[1]-q[1]
                if c0+d0>budget[0] or c1+d1>budget[1]:ok=False;break
            if not ok:continue
            sel.append(i)
            if rec(qmask&adj[i],eleft-(p==0),oleft-(p==1),c0+d0,c1+d1):return True
            sel.pop()
        return False
    found=rec((1<<n)-1,needE,needO,0,0)
    return found,(len(E),len(O),nodes)

def kclique(vals,k):
    n=len(vals);adj=[0]*n
    for i,j in combinations(range(n),2):
        if fd(vals[i],vals[j])==6:adj[i]|=1<<j;adj[j]|=1<<i
    def rec(mask,d):
        if d==k:return True
        if mask.bit_count()<k-d:return False
        q=mask
        while q:
            if q.bit_count()<k-d:return False
            l=q&-q;i=l.bit_length()-1;q-=l
            if rec(q&adj[i],d+1):return True
        return False
    return rec((1<<n)-1,0)

classes=[
 ('A2224',(0,0,0,0),(2,2,2,4),5,(1046,1040),[0,bits([0,1]),bits([0,2])]),
 ('B2244',(0,0,0,0),(2,2,4,4),5,(1033,1029),[0,bits([0,1]),bits([2,3])]),
 ('C2444',(0,0,0,0),(2,4,4,4),5,(1026,1032),[0,bits([0,1]),bits([0,2,3,4])]),
 ('D4244',(0,0,0,0),(4,2,4,4),5,(1026,1026),[0,bits([0,1,2,3]),bits([0,4])]),
 ('E2223',(0,0,0,1),(2,2,2,3),5,(1048,1037),[0,bits([0,1]),bits([0,2])]),
 ('F2332',(0,0,1,1),(2,3,3,2),6,(1026,1033),[0,bits([0,1]),bits([0,2,3])])]

active_orbits={}
for name,ap,ds,neven,U,base in classes:
    C=[]
    for x in range(N):
        if x in base or parity(x)!=ap[3]:continue
        if fd(base[2],x)!=ds[3]:continue
        if fd(base[0],x)!=(6 if ap[0]==ap[3] else 5):continue
        if fd(base[1],x)!=(6 if ap[1]==ap[3] else 5):continue
        C.append(x)
    bl=block_partition(base[1:])
    g=defaultdict(list)
    for x in C:g[sig_word(x,bl)].append(x)
    active_orbits[name]=g

assert sorted(map(len,active_orbits['A2224'].values()))==[126]
assert sorted(map(len,active_orbits['B2244'].values()))==[112]
assert sorted(map(len,active_orbits['C2444'].values()))==[21,105]
assert sorted(map(len,active_orbits['D4244'].values()))==[105]
assert sorted(map(len,active_orbits['E2223'].values()))==[84]
assert sorted(map(len,active_orbits['F2332'].values()))==[28]

name,ap,ds,neven,U,base=classes[0];x=next(iter(active_orbits[name].values()))[0];active=base+[x];budget=(22,16)
E=candidates(active,budget,0);assert len(E)==60
bl=block_partition(active[1:]);assert len({sig_word(y,bl) for y,_ in E})==1
e=E[0][0];assert active_def(active+[e])==(0,0)
found,stats=search_completion(active+[e],budget,0,7);assert not found

name,ap,ds,neven,U,base=classes[1];x=next(iter(active_orbits[name].values()))[0];active=base+[x];budget=(9,5)
E=candidates(active,budget,0);O=candidates(active,budget,1);assert len(E)==60
for e,_ in E:
    ov=[o for o,_ in O if fd(e,o)==5]
    assert not kclique(ov,7)

name,ap,ds,neven,U,base=classes[2];budget=(2,8)
stC=[]
for arr in active_orbits[name].values():
    active=base+[arr[0]]
    found,st=search_completion(active,budget,1,7);assert not found;stC.append((len(arr),st))
assert sorted(x for x,_ in stC)==[21,105]

name,ap,ds,neven,U,base=classes[3];budget=(2,2);arr=next(iter(active_orbits[name].values()));active=base+[arr[0]]
found,stD=search_completion(active,budget,1,7);assert not found

name,ap,ds,neven,U,base=classes[4];budget=(24,13);arr=next(iter(active_orbits[name].values()));active=base+[arr[0]]
Evals=[x for x,_ in candidates(active,budget,0)];bl=block_partition(active[1:]);P=[]
for a,b in combinations(Evals,2):
    if fd(a,b)==6 and active_def(active+[a,b])==(0,0):P.append((a,b))
assert len(P)==1740
g=defaultdict(list)
for a,b in P:g[pair_sig(a,b,bl)].append((a,b))
assert sorted(map(len,g.values()))==[30,270,360,540,540]
stE=[]
for rr in g.values():
    ext=active+list(rr[0]);found,st=search_completion(ext,budget,0,6);assert not found;stE.append((len(rr),st))

name,ap,ds,neven,U,base=classes[5];budget=(2,9);arr=next(iter(active_orbits[name].values()));active=base+[arr[0]]
E=candidates(active,budget,0);vals=[x for x,_ in E]
sol=[]
def rec4(prefix,cands):
    if len(prefix)==4:
        if active_def(active+prefix)==(0,0):sol.append(tuple(prefix))
        return
    for idx,x in enumerate(cands):
        nxt=[y for y in cands[idx+1:] if fd(x,y)==6]
        rec4(prefix+[x],nxt)
rec4([],vals)
assert len(sol)==5760
bl=block_partition(active[1:]);g=defaultdict(list)
for ws in sol:g[tuple_sig(ws,bl)].append(ws)
assert sorted(map(len,g.values()))==[720,720,1440,2880]
stF=[]
for rr in g.values():
    ext=active+list(rr[0]);found,st=search_completion(ext,budget,0,4);assert not found;stF.append((len(rr),st))

print('CERTIFICATE PASSED')
print('A (2224): active orbit 126; even-isolate orbit 60; DFS nodes',stats[2],'; no completion')
print('B (2244): active orbit 112; all 60 even choices have no odd d6 7-clique')
print('C (2444): active orbit sizes 21,105; both exact searches fail:',stC)
print('D (4244): active orbit 105; exact search fails:',stD)
print('E (2223 mixed pendant): even-pair orbit sizes 30,270,360,540,540; all fail:',stE)
print('F (2332 balanced mixed): even-4set orbit sizes 720,720,1440,2880; all fail:',stF)
print('CONCLUSION: all six triangle+pendant K=4 canonical classes are impossible')
