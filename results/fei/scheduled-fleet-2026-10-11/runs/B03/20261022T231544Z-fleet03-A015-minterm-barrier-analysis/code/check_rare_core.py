"""A015-RARE-CORE-QUEUE-CHECK@1. Independent exact finite checker."""
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
COUNT = 0

def check(ok, context):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(context)
    if time.monotonic()-START > 55:
        raise RuntimeError('Frozen 55-second CPU/wall budget exhausted')

def walsh(a):
    a = a[:]
    k = 1
    while k < len(a):
        for start in range(0,len(a),2*k):
            for j in range(start,start+k):
                u,v = a[j],a[j+k]
                a[j],a[j+k] = u+v,u-v
        k *= 2
    return a

def physical(m,t,r):
    n = 2*m+r
    L = 1<<n
    mask = (1<<m)-1
    vals = []
    for z in range(L):
        hit = ((z&mask).bit_count()>=m-t and
               ((z>>m)&mask).bit_count()>=m-t and
               (z>>(2*m))==(1<<r)-1)
        vals.append(2*int(hit)-1)
    a = walsh(vals)
    S = sum(math.comb(m,j) for j in range(t+1))
    q,p = F(S,1<<m),F(1,1<<r)
    b = q*q
    ig = 4*m*q*F(math.comb(m-1,t),1<<m)
    infl = sum(vals[z]!=vals[z^(1<<i)] for i in range(n) for z in range(L))
    check(F(infl,L)==p*(ig+2*r*b),('influence',m,t,r))
    check(F(a[0],L)==2*p*b-1,('mean',m,t,r))
    check(sum(v*v for v in a)==L*L,('parseval',m,t,r))
    v = F(sum(v*v for v in a[1:]),L*L)
    check(v==4*p*b*(1-p*b),('variance',m,t,r))
    check(n*v<=8*F(infl,L),('payment',m,t,r))
    # Separate tensor-factor derivation of every Fourier coefficient.
    small = walsh([int(z.bit_count()>=m-t) for z in range(1<<m)])
    for z,coef in enumerate(a):
        pred = 2*((-1)**((z>>(2*m)).bit_count()))*small[z&mask]*small[(z>>m)&mask]
        if z==0:
            pred -= L
        check(coef==pred,('tensor coefficient',m,t,r,z))
    return {'m':m,'t':t,'r':r,'n':n,'I':str(F(infl,L)),'variance':str(v)}

def root_interval(value):
    # Enclose the positive fifth root with rational endpoints of width 2^-64.
    scale=1<<64
    lo,hi=0,scale
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**5*value.denominator <= value.numerator*scale**5:
            lo=mid
        else:
            hi=mid
    if lo**5*value.denominator==value.numerator*scale**5:
        return F(lo,scale),F(lo,scale)
    return F(lo,scale),F(hi,scale)

def visits(W):
    ans={}
    for s in range(1,W+1):
        weights=[root_interval(min(F(1),F(s,j))**6) for j in range(1,W+1)]
        zlo,zhi=F(0),F(0)
        products={}
        for subset in itertools.combinations(range(W),s):
            lo=hi=F(1)
            mask=0
            for j in subset:
                lo*=weights[j][0];hi*=weights[j][1];mask|=1<<j
            products[mask]=(lo,hi)
            zlo+=lo;zhi+=hi
        for mask,(lo,hi) in products.items():
            interval=(lo/zhi/F(2*s*(s+1)),hi/zlo/F(2*s*(s+1)))
            check(interval[0]>=F(1,1<<(4*W)),('visit interval',W,s,mask))
            ans[mask]=interval
    return ans

def queue(m,t,r,cache):
    n=2*m+r
    controls=((1<<r)-1)<<(2*m)
    side=[sum(1<<j for j in c) for c in itertools.combinations(range(m),m-t)]
    gates=[x|(y<<m)|controls for x in side for y in side]
    N=len(gates);W=2*(m-t)+r;pi=F(1,1<<W);z=pi/N
    roots=[gates[0]] if t==0 else [
        (((1<<m)-1)^((1<<t)-1)) | ((((1<<m)-1)^((1<<t)-1))<<m)|controls,
        (((1<<m)-1)^(((1<<t)-1)<<t)) | ((((1<<m)-1)^(((1<<t)-1)<<t))<<m)|controls]
    check(all(g in gates for g in roots),('original gates',m,t,r))
    cover=0
    for g in roots:cover|=g
    check(cover==(1<<n)-1,('cover',m,t,r))
    if W not in cache:cache[W]=visits(W)
    D=(1+z)**N-1
    check(0<D<=2*pi,('normalizer',m,t,r))
    total_hi=F(0)
    minimum=None
    for output in range(1,1<<n):
        remaining=output
        blocks=[]
        for g in roots:
            b=remaining&g
            if b:
                positions=[i for i in range(n) if g>>i&1]
                local=sum(1<<j for j,i in enumerate(positions) if b>>i&1)
                blocks.append(local)
                remaining ^= b
        check(remaining==0,('partition',m,t,r,output))
        c=len(blocks)
        rp=z**c/D
        direct=(z/(1+z))**c*(1/(1+z))**(N-c)/(1-(1+z)**(-N))
        check(rp==direct,('inclusion absence',m,t,r,output))
        lo=hi=rp
        for block in blocks:
            lo*=cache[W][block][0];hi*=cache[W][block][1]
        check(lo>=F(1,1<<(12*n)),('complete queue bound',m,t,r,output))
        total_hi+=hi
        if minimum is None or lo<minimum:minimum=lo
    check(total_hi<=1,('selected subprobability',m,t,r))
    return {'m':m,'t':t,'r':r,'N':N,'W':W,'outputs':(1<<n)-1,
            'minimum_Q_lower':str(minimum),'selected_total_upper':str(total_hi)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    physical_cases=[(m,t,r) for m in range(2,4 if args.pilot else 7)
                    for t in range(max(1,m//4)+1) for r in range(2 if args.pilot else 3)]
    if not args.pilot:physical_cases.append((8,2,0))
    result={'helper':'A015-RARE-CORE-QUEUE-CHECK@1','pilot':args.pilot,
            'physical':[physical(*case) for case in physical_cases]}
    if not args.pilot:
        scalar_count=0
        for m in range(2,65):
            for t in range(max(1,m//4)+1):
                S=sum(math.comb(m,j) for j in range(t+1))
                q=F(S,1<<m);b=q*q;ig=4*m*q*F(math.comb(m-1,t),1<<m)
                check(ig>=m*b,('tail influence',m,t))
                check(b<=F(9,16),('core mass',m,t))
                if t<=m//4:
                    check(S<=F(math.comb(m,t)*(m-t+1),m-2*t+1),('geometric tail',m,t))
                for r in range(9):
                    scalar_count+=1;p=F(1,1<<r);n=2*m+r;W=2*(m-t)+r
                    var=4*p*b*(1-p*b);I=p*(ig+2*r*b)
                    check(n*var<=8*I,('scalar payment',m,t,r))
                    check(var>=F(1,1<<n),('variance floor',m,t,r))
                    check((F(n)+F(3,2))*var<=11*I,('entropy correction',m,t,r))
                    N=math.comb(m,t)**2
                    check(2*N*N*(1<<(9*W))<=1<<(12*n),('dimension exponent',m,t,r))
        for W in range(1,65):
            for s in range(1,W+1):
                # Raise positive visit bound to the fifth power; exact rational acceptance.
                lo5=F(s,W)**(6*s)/F(2*s*(s+1)*2**W)**5
                check(lo5>=F(1,1<<(20*W)),('visit fifth power',W,s))
        cache={}
        result['queue']=[queue(m,t,r,cache) for m in range(2,5) for t in range(2) for r in range(2)]
        result['scalar_cases']=scalar_count
        result['visit_pairs']=2080
    result['assertions']=COUNT
    result['elapsed_seconds']=round(time.monotonic()-START,3)
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    name='pilot.json' if args.pilot else 'checks.json'
    out=ROOT/'out';out.mkdir(exist_ok=True)
    (out/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','output':str(out/name),'assertions':COUNT,
                      'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
