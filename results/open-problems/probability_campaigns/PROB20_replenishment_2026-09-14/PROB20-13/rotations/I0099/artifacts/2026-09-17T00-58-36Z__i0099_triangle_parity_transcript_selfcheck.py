#!/usr/bin/env python3
from itertools import combinations
from pathlib import Path
import re, sys, gzip, base64, hashlib

TRANSCRIPT = Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/2026-09-17T00-58-36Z__i0099_p3613_exact_transcript.out')

def qr_bool(p):
    q=[False]*p
    for x in range(1,p): q[(x*x)%p]=True
    return q

def chi(x,p,qr):
    x%=p
    if x==0: return 0
    return 1 if qr[x] else -1

def sqrt_table(p):
    d={}
    for x in range(p): d.setdefault((x*x)%p,x)
    return d

def max_clique_small(p,qr):
    adj=[set() for _ in range(p)]
    for i in range(p):
        for j in range(i+1,p):
            if qr[(i-j)%p]: adj[i].add(j); adj[j].add(i)
    best=[]
    def rec(R,P):
        nonlocal best
        if len(R)+len(P)<=len(best): return
        if not P:
            if len(R)>len(best): best=R[:]
            return
        order=sorted(P, key=lambda v:len(P & adj[v]), reverse=True)
        Pset=set(P)
        for v in order:
            if v not in Pset: continue
            rec(R+[v], Pset & adj[v])
            Pset.remove(v)
            if len(R)+len(Pset)<=len(best): return
    rec([],set(range(p)))
    return best,adj

def check_small_prime(p):
    qr=qr_bool(p); roots=sqrt_table(p)
    assert p%4==1
    clique,adj=max_clique_small(p,qr)
    tri=0
    for a in range(p):
      for b in adj[a]:
        if b<=a: continue
        for c in adj[a] & adj[b]:
          if c<=b: continue
          tri+=1
          S=sum(chi((x-a)*(x-b)*(x-c),p,qr) for x in range(p))
          N=p+1+S
          common=len(adj[a] & adj[b] & adj[c])
          assert N%16==0, (p,a,b,c,N)
          assert common%2==0, (p,a,b,c,common)
          assert 8*common==N-16, (p,a,b,c,common,N)
          r=roots[(a-b)%p]; s=roots[(a-c)%p]
          x0=(a+r*s)%p; y0=(r*s*(r+s))%p
          assert y0!=0
          assert (y0*y0-(x0-a)*(x0-b)*(x0-c))%p==0
          m=(r+s)%p
          x2=(m*m + (a+b+c) - 2*x0)%p
          assert x2==a
    assert tri>0

    C=clique; k=len(C); ext=set(range(p))-set(C)
    A=[]
    for c in C:
        A.append({x for x in ext if chi(x-c,p,qr)==-1})
    q=(p-1)//4
    for i in range(k): assert len(A[i])==(p-1)//2
    for i,j in combinations(range(k),2): assert len(A[i]&A[j])==q
    for i,j,l in combinations(range(k),3): assert len(A[i]&A[j]&A[l])%2==q%2
    for mask in range(1<<k):
        J=[i for i in range(k) if (mask>>i)&1]
        v=set()
        for i in J: v ^= A[i]
        m=len(J)
        c2=m*(m-1)//2; c3=m*(m-1)*(m-2)//6
        rhs=(2*q*(m-c2)+4*(q%2)*c3)%8
        assert len(v)%8==rhs,(p,C,J,len(v),rhs)
    print(f'SMALL_PRIME_PASS p={p} triangles={tri} clique_size={k} clique={C}')

def inv(x,p): return pow(x,p-2,p)

def s3_reps(p,vals,idx):
    n=len(vals); seen=[False]*n; reps=[]
    def s(i): return idx[(1-vals[i])%p]
    def t(i): return idx[inv(vals[i],p)]
    for i in range(n):
        if seen[i]: continue
        stack=[i]; seen[i]=True; mem=[]
        while stack:
            v=stack.pop(); mem.append(v)
            for w in (s(v),t(v)):
                assert w>=0
                if not seen[w]: seen[w]=True; stack.append(w)
        reps.append(min(mem,key=lambda j:vals[j]))
    return reps

def v4_orbit_count(p,vals,idx,K,u):
    Kset=set(K); seen=set(); count=0
    def a(j): return idx[(u*inv(vals[j],p))%p]
    def b(j): return idx[((vals[j]-u)%p)*inv((vals[j]-1)%p,p)%p]
    for j in sorted(K):
        if j in seen: continue
        count+=1; stack=[j]; seen.add(j)
        while stack:
            v=stack.pop()
            for w in (a(v),b(v)):
                assert w in Kset
                if w not in seen: seen.add(w); stack.append(w)
    return count

def check_transcript():
    p=3613; omega=15; qr=qr_bool(p)
    vals=[x for x in range(2,p) if qr[x] and qr[(x-1)%p]]
    assert len(vals)==902
    idx=[-1]*p
    for i,x in enumerate(vals): idx[x]=i
    reps=s3_reps(p,vals,idx)
    assert len(reps)==151
    payload=TRANSCRIPT.read_text()
    if payload.startswith('I0099_EXECUTED_TRANSCRIPT_ENCODING=gzip+base64'):
        lines=payload.splitlines()
        want=re.match(r'RAW_SHA256=([0-9a-f]{64})',lines[1]).group(1)
        raw=gzip.decompress(base64.b64decode(''.join(lines[4:])))
        assert hashlib.sha256(raw).hexdigest()==want
        text=raw.decode()
    else:
        text=payload
    h=re.search(r'^I0099_V4_CERT p=(\d+) omega=(\d+) Hn=(\d+) s3reps=(\d+) witness=([0-9,]+) witness_nodes=(\d+)$',text,re.M)
    assert h
    hp,hom,hn,hs=map(int,h.group(1,2,3,4)); W=list(map(int,h.group(5).split(',')))
    assert (hp,hom,hn,hs)==(p,omega,902,151) and len(W)==omega and W[:2]==[0,1]
    for a,b in combinations(W,2): assert qr[(a-b)%p]
    silines=re.findall(r'^si=(\d+) u=(\d+) K=(\d+) v4reps=(\d+) no_nodes=(\d+)$',text,re.M)
    certs=re.findall(r'^CERTIFIED_V4_RANGE p=3613 omega=15 s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) seconds=([0-9.]+)$',text,re.M)
    assert len(silines)==len(certs)==151
    ob=nodes=0
    for z in range(151):
        si,u,Ksz,nv,nn=map(int,silines[z]); a,b,o,n=map(int,certs[z][:4])
        assert si==z and (a,b)==(z,z+1)
        assert u==vals[reps[z]]
        ui=reps[z]
        K=[j for j,x in enumerate(vals) if qr[(x-u)%p]]
        assert len(K)==Ksz
        assert v4_orbit_count(p,vals,idx,K,u)==nv==o
        assert nn==n
        ob+=o; nodes+=n
    assert ob==17031 and nodes==244854031
    ag=re.search(r'^AGGREGATE p=3613 omega=15 ranges=151 obligations=(\d+) total_nodes=(\d+) all_exit_codes_zero=1$',text,re.M)
    assert ag and tuple(map(int,ag.groups()))==(ob,nodes)
    print(f'P3613_TRANSCRIPT_STRUCTURAL_PASS Hn=902 s3reps=151 obligations={ob} total_nodes={nodes}')
    print('NOTE=Transcript audit independently checks graph arithmetic, witness, S3/V4 orbit structure, range partition, and totals; it does not rerun all branch-and-bound nodes.')

if __name__=='__main__':
    for p in [13,17,29,37,41,53,61,73,89,97]: check_small_prime(p)
    check_transcript()
    print('ALL_I0099_TRIANGLE_PARITY_AND_P3613_AUDITS_PASS')
