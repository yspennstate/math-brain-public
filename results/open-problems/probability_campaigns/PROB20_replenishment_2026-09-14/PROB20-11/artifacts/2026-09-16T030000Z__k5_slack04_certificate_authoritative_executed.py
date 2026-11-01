#!/usr/bin/env python3
"""PROB20-11 exact certificate: all canonical K=5 slack-(0,4) states fail at active stage."""
from itertools import combinations, permutations, product
from math import comb
N=2048
def fd(a,b):
    w=(a^b).bit_count(); return min(w,12-w)
def par(x): return x.bit_count()&1
B0=[x for x in range(N) if fd(0,x)<=3]; assert len(B0)==299
balls=[]
for c in range(N):
    m=0
    for b in B0:m|=1<<(c^b)
    balls.append(m)
EVEN=sum(1<<x for x in range(N) if par(x)==0); ODD=((1<<N)-1)^EVEN
def halves(m): return ((m&EVEN).bit_count(),(m&ODD).bit_count())
def pairh(a,b): return halves(balls[a]&balls[b])
def trih(a,b,c): return halves(balls[a]&balls[b]&balls[c])
trimax={}
for b in range(1,N):
    bb=balls[0]&balls[b]
    for c in range(b+1,N):
        k=(0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c)); h=halves(bb&balls[c]); old=trimax.get(k,(-1,-1)); trimax[k]=(max(old[0],h[0]),max(old[1],h[1]))
for k,h in list(trimax.items()):
    p0,p1,p2,a,b,c=k; trimax[(1,1-p1,1-p2,a,b,c)]=(h[1],h[0])
def tmax(p0,p1,p2,a,b,c):
    ps=(p0,p1,p2);D=((0,a,b),(a,0,c),(b,c,0))
    for q in permutations(range(3)):
        k=(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]])
        if k in trimax:return trimax[k]
    raise AssertionError(k)
def tm(a,b,c): return tmax(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c))
pairB={(0,0):(0,40),(0,1):(10,10),(1,0):(10,10),(1,1):(40,0)}
pairD={}
for p in (0,1):
    a=0 if p==0 else 1
    for q in (0,1):
        for d in ((2,4) if p==q else (1,3)):
            v={pairh(a,b) for b in range(N) if b!=a and par(b)==q and fd(a,b)==d};assert len(v)==1;pairD[p,q,d]=next(iter(v))
baseTri={}
for ps in product((0,1),repeat=3):
    ds=(6 if ps[0]==ps[1] else 5,6 if ps[0]==ps[2] else 5,6 if ps[1]==ps[2] else 5);baseTri[ps]=tmax(*ps,*ds)
def coarse_U(nv,es,ap,ds,ne):
    no=12-ne;S1=[67*ne+232*no,232*ne+67*no];S2=[comb(no,2)*40+ne*no*10,comb(ne,2)*40+ne*no*10];S3=[ne*comb(no,2)+4*comb(no,3),4*comb(ne,3)+comb(ne,2)*no]
    ed={tuple(sorted(e)):d for e,d in zip(es,ds)}
    for (i,j),d in zip(es,ds):
        a=pairD[ap[i],ap[j],d];b=pairB[ap[i],ap[j]]
        for h in (0,1):S2[h]+=a[h]-b[h]
    for i,j,k in combinations(range(nv),3):
        ij,jk,ik=tuple(sorted((i,j))),tuple(sorted((j,k))),tuple(sorted((i,k)))
        if not ({ij,jk,ik}&set(ed)):continue
        dij=ed.get(ij,6 if ap[i]==ap[j] else 5);dik=ed.get(ik,6 if ap[i]==ap[k] else 5);djk=ed.get(jk,6 if ap[j]==ap[k] else 5)
        a=tmax(ap[i],ap[j],ap[k],dij,dik,djk);b=baseTri[ap[i],ap[j],ap[k]]
        for h in (0,1):S3[h]+=a[h]-b[h]
    ie=ne-sum(p==0 for p in ap);io=12-nv-ie;assert ie>=0 and io>=0
    for (i,j),d in zip(es,ds):
        for q,n in ((0,ie),(1,io)):
            if n:
                a=tmax(ap[i],ap[j],q,d,6 if ap[i]==q else 5,6 if ap[j]==q else 5);b=baseTri[ap[i],ap[j],q]
                for h in (0,1):S3[h]+=n*(a[h]-b[h])
    return tuple(S1[h]-S2[h]+S3[h] for h in (0,1))
ST=[
("P3+K13",7,[(0,1),(0,2),(3,6),(4,6),(5,6)],(1,1,1,1,0,0,0),(4,2,3,4,4),6,(1028,1024),252),
("e5_2",5,[(0,1),(0,2),(0,4),(1,2),(2,3)],(1,1,1,1,0),(2,4,3,4,4),7,(1024,1028),240)]
def search(st):
    name,nv,es,ap,ds,ne,U,expect=st;assert coarse_U(nv,es,ap,ds,ne)==U
    ed={tuple(sorted(e)):d for e,d in zip(es,ds)};D=[[0]*nv for _ in range(nv)]
    for i in range(nv):
        for j in range(i+1,nv):D[i][j]=D[j][i]=ed.get((i,j),6 if ap[i]==ap[j] else 5)
    deg=[0]*nv
    for i,j in es:deg[i]+=1;deg[j]+=1
    root=max(range(nv),key=lambda i:(deg[i],-ap[i]));first=min((j for j in range(nv) if tuple(sorted((root,j))) in ed),key=lambda j:D[root][j])
    order=[root,first];used=set(order)
    while len(order)<nv:
        v=max((x for x in range(nv) if x not in used),key=lambda x:(sum(D[x][u]<=4 for u in order),deg[x],-D[root][x]));order.append(v);used.add(v)
    ap2=[ap[i] for i in order];D2=[[D[i][j] for j in order] for i in order];budget=[U[0]-1024,U[1]-1024]
    flip=ap2[0]
    if flip:ap2=[1-p for p in ap2];budget.reverse()
    z1=(1<<D2[0][1])-1;assert par(z1)==ap2[1]
    cand=[[z for z in range(N) if par(z)==ap2[k] and fd(0,z)==D2[0][k]] for k in range(nv)]
    chosen=[0,z1];cnt=[0]*N
    for z in chosen:
        m=balls[z]
        while m:
            l=m&-m;x=l.bit_length()-1;cnt[x]+=1;m-=l
    nodes=[0]*13
    def rec(k,de,do,ee,eo):
        nodes[k]+=1
        if k==nv:return 1
        total=0
        for z in cand[k]:
            if z in chosen or any(fd(z,a)!=D2[k][j] for j,a in enumerate(chosen)):continue
            nde,ndo,nee,neo=de,do,ee,eo
            bad=False
            for a,b in combinations(chosen,2):
                ac=trih(a,b,z);mx=tm(a,b,z);nde+=mx[0]-ac[0];ndo+=mx[1]-ac[1]
                if nde+nee>budget[0] or ndo+neo>budget[1]:bad=True;break
            if bad:continue
            touched=[];m=balls[z]
            while m:
                l=m&-m;x=l.bit_length()-1;m-=l;touched.append(x);old=cnt[x]
                if old>=3:
                    inc=(old-1)*(old-2)//2
                    if par(x):neo+=inc
                    else:nee+=inc
            if nde+nee>budget[0] or ndo+neo>budget[1]:continue
            chosen.append(z)
            for x in touched:cnt[x]+=1
            total+=rec(k+1,nde,ndo,nee,neo)
            for x in touched:cnt[x]-=1
            chosen.pop()
        return total
    survivors=rec(2,0,0,0,0);assert survivors==0 and nodes[2]==1 and nodes[3]==expect and all(nodes[k]==0 for k in range(4,nv+1))
    print(name,U,"budget",tuple(budget),"nodes2",nodes[2],"nodes3",nodes[3],"survivors",survivors)
for st in ST:search(st)
print("K5 SLACK-(0,4) TWO-STATE CERTIFICATE PASSED")
