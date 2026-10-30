"""Frozen exact checks; no author implementation imported, no floating signs."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import factorial
import argparse, json, time

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
OUT.mkdir(exist_ok=True)
checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def save(name,d):
    (OUT/name).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def fwht(a):
    a=list(a); s=1
    while s<len(a):
        for j in range(0,len(a),2*s):
            for i in range(j,j+s):
                x,y=a[i],a[i+s]; a[i],a[i+s]=x+y,x-y
        s*=2
    return a
def faces(n):
    ans=[]
    for R in range(1,1<<n):
        w=R.bit_count()
        a=R
        while True:
            mask=sum(1<<x for x in range(1<<n) if x&R==a)
            ans.append((R,w,a,mask))
            if a==0: break
            a=(a-1)&R
    return ans
def universal(ns):
    rows=[]
    for n in ns:
        N=1<<n; fs=faces(n); cases=0; gates=0; sharp=0; packed=0
        for t in range(1<<N):
            false=N-t.bit_count()
            e=[sum(((t>>x)^(t>>(x^(1<<i))))&1 for x in range(N) if not x&(1<<i)) for i in range(n)]
            eligible=[]
            for R,w,a,mask in fs:
                if t&mask==mask:
                    ei=sum(e[i] for i in range(n) if R&(1<<i))
                    ck(ei*((1<<w)-1)>=false*w)
                    sharp+=int(ei*((1<<w)-1)==false*w and false>0)
                    gates+=1;eligible.append((R,w))
            if false and eligible:
                reads=[sum(bool(R&(1<<i)) for R,w in eligible) for i in range(n)]
                M=max(reads); sn=sum(1<<(n-w) for R,w in eligible)
                ck(2*false*sn<=N*M*sum(e));packed+=1
                wide=[(R,w) for R,w in eligible if w>=2]
                if wide:
                    M2=max(sum(bool(R&(1<<i)) for R,w in wide) for i in range(n))
                    sn2=sum(1<<(n-w) for R,w in wide)
                    ck(8*false*sn2<=3*N*M2*sum(e))
            if n<=3:
                vals=[1 if t>>x&1 else -1 for x in range(N)]
                wh=fwht(vals)
                ck(sum(z*z for z in wh)==N*N)
                for i in range(n): ck(sum(wh[A]**2 for A in range(N) if A&(1<<i))==2*e[i]*N)
            cases+=1
        # Check the exact minimum-cut fact independently over all proper subsets.
        for t in range(1,(1<<N)-1):
            boundary=sum(((t>>x)^(t>>(x^(1<<i))))&1 for i in range(n) for x in range(N) if not x&(1<<i))
            ck(boundary>=n)
        row=dict(n=n,functions=cases,implicants=gates,nonconstant_sharp_faces=sharp,packed_tables=packed)
        rows.append(row); save('UNIVERSAL_PARTIAL.json',dict(rows=rows,checks=checks))
    return rows

def block_trace(h,chosen,m,ell):
    # Enumerate root identity and every actual child-label chronology.
    if not h: return (ell/F(4)*F(1,4)*F(1,2))**len(chosen)
    if not chosen:
        return sum((ell/F(4)*F(1,4)*F(1,2) for root in range(m)),F(0))
    t=len(chosen); ans=F(0)
    for root in chosen:
        children=[x for x in chosen if x!=root]
        for chronology in permutations(children):
            z=ell/F(4)*F(1,6)*F(1,t*(t+1))*F(1,t)
            for child in chronology: z*=ell*F(1,4)*F(1,2)
            ans+=z
    return ans
def block_formula(h,t,m):
    ell=F(1,2*m)
    if not h:return (ell/32)**t
    if not t:return F(1,64)
    return F(factorial(t),24*8**(t-1)*t*t*(t+1))*ell**t
def private(pilot):
    rows=[]
    for r in ([1,2] if pilot else [1,2,3]):
        pairs=list(combinations(range(r),2))
        for em in range(1<<len(pairs)):
            core=[e for j,e in enumerate(pairs) if em>>j&1]
            for ms in product([1,2],repeat=r):
                edges=list(core);leaves=[];n=r
                for i,m in enumerate(ms):
                    li=list(range(n,n+m));n+=m;leaves.append(li);edges.extend((i,j) for j in li)
                N=1<<n
                vals=[1 if any(x>>i&1 and x>>j&1 for i,j in edges) else -1 for x in range(N)]
                wh=fwht(vals);ck(sum(z*z for z in wh)==N*N)
                inf=[F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N) for i in range(n)]
                ck(sum(inf)==F(sum(A.bit_count()*wh[A]**2 for A in range(N)),N*N))
                q=F(vals.count(-1),N);I=sum(inf);ck(q>0 and I>0)
                deg=[sum(i in e for e in core) for i in range(r)]
                weights=[F(1,2*max(deg[i],deg[j])) for i,j in core]
                weights.extend(F(1,2*ms[i]) for i in range(r) for j in leaves[i])
                for i in range(n):ck(sum(l for e,l in zip(edges,weights) if i in e)<=1)
                D=F(1)
                for ell in weights:D*=1+ell/4
                D-=1;ck(D>0)
                ck(sum(weights)<=F(3*r,4))
                for i,m in enumerate(ms):
                    a=F(sum(vals[x]==-1 and not x>>i&1 for x in range(N)),N)
                    b=F(sum(vals[x]==-1 and x>>i&1 for x in range(N)),N)
                    ck(a+b==q);ck(b<=a/F(2**m));ck(inf[i]==2*(a-b));ck(inf[i]>=a);ck(inf[i]>=2*q/3)
                    for j in leaves[i]:ck(inf[j]==2*b)
                ck(I>=2*r*q/3)
                mass=F(0)
                for A in range(1,N):
                    num=F(1); lower=F(1,96**A.bit_count())
                    for i,m in enumerate(ms):
                        h=int(bool(A>>i&1)); chosen=[j for j in leaves[i] if A>>j&1];t=len(chosen)
                        u=block_trace(h,chosen,m,F(1,2*m));ck(u==block_formula(h,t,m));ck(u>=F(1,96**(h+t)*m**t))
                        num*=u;lower/=m**t
                    ck(num>=lower and num>0);mass+=num/D
                ck(mass<=1)
                rows.append(dict(hubs=r,core=core,private_counts=ms,dimension=n,influence=str(I),false_probability=str(q),normalizer=str(D),reference_mass=str(mass)))
                with (OUT/'PRIVATE_PARTIAL.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(rows[-1])+'\n')
    for m in range(1,129):
        ck(F(m*m,2**m)<=F(9,8));ck((m+1)**2<=2*m*m if m>=3 else True)
        for t in range(m+1):
            for h in [0,1]:ck(block_formula(h,t,m)>=F(1,96**(h+t)*m**t))
    # Shared neighbors destroy the private-leaf hypothesis: K_(r,m).
    # Exact independent-set counts give b/a with one named hub.
    shared=[]
    for r,m in [(2,1),(3,2),(5,2),(2,5)]:
        den=2**(r+m);a=F(2**m+2**(r-1)-1,den);b=F(2**(r-1),den)
        if r>=2:ck(b>F(1,2**m)*a)
        shared.append(dict(r=r,m=m,b_over_a=str(b/a),private_surrogate=str(F(1,2**m))))
    return rows,shared

def main():
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');args=p.parse_args()
    start=time.perf_counter();u=universal([1,2,3] if args.pilot else [4]);pr,sh=private(args.pilot)
    elapsed=time.perf_counter()-start
    result=dict(status='PASS',arithmetic='integer/Fraction',universal=u,private_functions=len(pr),shared_neighbor_witnesses=sh,exact_assertions=checks,elapsed_seconds=elapsed)
    save('PILOT.json' if args.pilot else 'CHECK.json',result)
    print(json.dumps(result))
if __name__=='__main__':main()
