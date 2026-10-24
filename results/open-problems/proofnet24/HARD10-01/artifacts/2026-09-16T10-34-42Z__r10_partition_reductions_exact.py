#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def norm(e): return tuple(sorted(e))

def comps(n, edges, mask):
    p=list(range(n)); r=[0]*n
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(a,b) in enumerate(edges):
        if not ((mask>>i)&1): continue
        a,b=f(a),f(b)
        if a==b: return None
        if r[a]<r[b]: a,b=b,a
        p[b]=a
        if r[a]==r[b]: r[a]+=1
    return [f(i) for i in range(n)]

def fixed_R(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H); R=bytearray(N); root=bytearray(N)
    a,b=e; c,d=f
    for m in range(N):
        C=comps(n,H,m)
        if C is None: continue
        ra,rb,rc,rd=C[a],C[b],C[c],C[d]
        if ra!=rb and rc!=rd and {ra,rb}=={rc,rd}: R[m]=1
    for m in range(N):
        if not R[m]: continue
        x=m
        while x:
            bit=x&-x
            if R[m^bit]: break
            x-=bit
        else: root[m]=1
    cnt=list(R)
    for i in range(len(H)):
        bit=1<<i
        for m in range(N):
            if m&bit: cnt[m]+=cnt[m^bit]
    return H,R,root,cnt

def fiber_partition(M,R,root):
    rs=[m for m,x in enumerate(R) if x and not(m&~M)]
    roots=[m for m,x in enumerate(root) if x and not(m&~M)]
    fs=[sum(1 for A in rs if not(m&~A)) for m in roots]
    return tuple(sorted(fs,reverse=True)),rs,roots

def r10_counts(n,e,f):
    H,R,root,cnt=fixed_R(n,e,f); C=Counter()
    for M,v in enumerate(cnt):
        if v==10:
            part,_,_=fiber_partition(M,R,root); C[part]+=1
    return C

def partitions(n,maxp=None):
    if n==0:
        yield (); return
    if maxp is None or maxp>n: maxp=n
    for k in range(maxp,0,-1):
        for q in partitions(n-k,k): yield (k,)+q

def possible_allminimal(N,inc):
    facts=[]
    for a in range(2,N+1):
        if N%a: continue
        b=N//a
        if a>b or b<2: continue
        facts.append((a,b, inc%a==0 or inc%b==0))
    return facts

def bit_edge(H,b): return H[b.bit_length()-1]
def star_info(H,P,F):
    atoms=[]
    for A in F:
        d=A^P
        if d and not(d&(d-1)): atoms.append(d)
    if len(F)!=4 or len(atoms)!=3: return None
    E=[bit_edge(H,b) for b in atoms]
    common=set(E[0])&set(E[1])&set(E[2])
    if len(common)!=1:return None
    w=next(iter(common)); at=[]
    for a,b in E: at.append(b if a==w else a)
    return w,tuple(sorted(at))
def edges_of(H,m): return {H[i] for i in range(len(H)) if (m>>i)&1}

def gap(n,M,H,e,f):
    edges=[e,f]+[H[i] for i in range(len(H)) if (M>>i)&1]
    edges=list(dict.fromkeys(map(norm,edges)))
    ie=edges.index(norm(e)); jf=edges.index(norm(f))
    Z=Ze=Zf=Zef=0
    for m in range(1<<len(edges)):
        if comps(n,edges,m) is None: continue
        Z+=1; a=(m>>ie)&1; b=(m>>jf)&1
        Ze+=a; Zf+=b; Zef+=a*b
    return Ze*Zf-Z*Zef

def classify_4411_n6():
    n=6;e=(0,1);f=(2,3)
    H,R,root,cnt=fixed_R(n,e,f)
    out=Counter(); total=0
    for M,v in enumerate(cnt):
        if v!=10: continue
        part,rs,roots=fiber_partition(M,R,root)
        if part!=(4,4,1,1):continue
        fib={p:[A for A in rs if not(p&~A)] for p in roots}
        L=[p for p in roots if len(fib[p])==4]; S=[p for p in roots if len(fib[p])==1]
        I=[star_info(H,p,fib[p]) for p in L]
        assert all(x is not None for x in I)
        (w,A),(x,B)=I
        g=gap(n,M,H,e,f)
        if w==x:
            pairs=[]
            for s in S:
                cyc=edges_of(H,s)|{norm(e),norm(f)}
                pairs.append(tuple(sorted(a for a in A if norm((w,a)) in cyc)))
            regime='same-center/same-pair' if pairs[0]==pairs[1] else 'same-center/distinct-pairs'
        else:
            P,Q=L; CP=edges_of(H,P)|{norm(e),norm(f)}; CQ=edges_of(H,Q)|{norm(e),norm(f)}
            tA=set(a for a in A if norm((w,a)) in CQ)
            tB=set(b for b in B if norm((x,b)) in CP)
            connector=norm((w,x)) in edges_of(H,M)
            inter=len(tA&tB)
            if connector and inter==2: regime='distinct/connector/same-ear-pair'
            elif connector and inter==1: regime='distinct/connector/ear-pairs-share-one'
            elif (not connector) and inter==1: regime='distinct/no-connector/ear-pairs-share-one'
            else: regime=f'distinct/other(conn={connector},inter={inter})'
        out[(regime,g)]+=1; total+=1
    assert total==116
    return out

def main():
    print('R10 n6 adjacent',dict(r10_counts(6,(0,1),(0,2))))
    print('R10 n6 disjoint',dict(r10_counts(6,(0,1),(2,3))))
    candidates=[p for p in partitions(10) if 2 not in p]
    print('integer partitions of 10 without part 2:',candidates)
    for m in range(2,8):
        print('all-minimal obstruction m=',m,'N=',m+1,'factorizations=',possible_allminimal(m+1,m))
    regimes=classify_4411_n6()
    print('4+4+1+1 n6 regimes:')
    for k,v in sorted(regimes.items()): print(' ',k,v)
    assert set(g for (_,g) in regimes) == {124,248,264,280,288,480}
    print('OK')
if __name__=='__main__': main()
