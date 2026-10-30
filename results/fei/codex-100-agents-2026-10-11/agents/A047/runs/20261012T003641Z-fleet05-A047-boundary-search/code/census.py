from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import isqrt
import json,time,argparse

R=Path(__file__).resolve().parents[1]; SCALE=1<<100; CLOCK=time.monotonic()
def walsh(t):
    a=list(t); s=1
    while s<len(a):
        for k in range(0,len(a),2*s):
            for j in range(s):
                u,v=a[k+j],a[k+j+s]; a[k+j],a[k+j+s]=u+v,u-v
        s*=2
    return tuple(a)
def direct(t):
    return tuple(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t)))
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1); zz=z*z; a=z; total=F(0)
    for k in range(40): total+=2*a/(2*k+1); a*=zz
    return total,total+2*a/(81*(1-zz))
@lru_cache(None)
def logi(x):
    assert x>0; k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    lo,hi=ln_unit(x); dl,dh=ln_unit(F(2))
    return F(k)+lo/dh,F(k)+hi/dl
def floor(x): return x.numerator//x.denominator
def ceil(x): return -floor(-x)
@lru_cache(None)
def eta(x):
    assert 0<=x<=1
    if not x:return (0,0)
    lo,hi=logi(x)
    return floor(-x*hi*SCALE),ceil(-x*lo*SCALE)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,x):
    vals=[F(a[0])*x,F(a[1])*x];return floor(min(vals)),ceil(max(vals))
def hb(x):return add(eta(x),eta(1-x))
def record(a):return {'lower':str(F(a[0],SCALE)),'upper':str(F(a[1],SCALE)),'display':[a[0]/SCALE,a[1]/SCALE]}
def factors(n):
    ans={};d=2
    while d*d<=n:
        while n%d==0:ans[d]=ans.get(d,0)+1;n//=d
        d+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
@lru_cache(None)
def symbolic_fiber(u,v,N,p):
    G,H=F(u,N),F(v,N);a=((1-p)*G+p*H)**2;b=p*(1-p)*(H-G)**2;q=a+b;ans={}
    for s,c in ((q,F(2)),(a,F(-1)),(b,F(-1)),(G*G,-(1-p)),(H*H,-p)):
        if not s:continue
        for sign,n in ((1,s.numerator),(-1,s.denominator)):
            for prime,k in factors(n).items():ans[prime]=ans.get(prime,F(0))-c*s*sign*k
    return tuple(sorted((k,v) for k,v in ans.items() if v))
def symbolic_pair(G,H,N,p):
    ans={}
    for u,v in zip(G,H):
        for prime,c in symbolic_fiber(u,v,N,p):ans[prime]=ans.get(prime,F(0))+c
    return tuple(sorted((k,v) for k,v in ans.items() if v))
@lru_cache(None)
def fiber(u,v,N,p):
    g,h=F(u,N),F(v,N)
    a=((1-p)*g+p*h)**2;b=p*(1-p)*(h-g)**2;q=(1-p)*g*g+p*h*h
    assert a+b==q
    return sub(sub(sub(scale(eta(q),2),add(eta(a),eta(b))),scale(eta(g*g),1-p)),scale(eta(h*h),p))
def sqrt_i(x):
    assert x>=0; Q=1<<140; z=isqrt((x.numerator*Q*Q)//x.denominator)
    lo=F(z,Q);hi=F(z+1,Q)
    assert lo*lo<=x<=hi*hi
    return lo,hi
def real_witness(p,x):
    # y=sin^2(t-b), with sin^2 t=x and t,b in [0,pi/4].
    assert 0<=x<=p<F(1,2)
    lo,hi=sqrt_i(p*(1-p)*x*(1-x)); base=p+(1-2*p)*x
    yl=max(F(0),base-2*hi); yh=min(F(1,2),base-2*lo)
    assert 0<=yl<=yh<=F(1,2)
    # h2 is increasing on [0,1/2].
    Hy=(hb(yl)[0],hb(yh)[1]); D=sub(sub(hb(p),hb(x)),Hy)
    return {'x':str(x),'y_interval':[str(yl),str(yh)],'debt':record(D),'raw_lower':D[0]}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--max-n',type=int,choices=[2,3],required=True);a=parser.parse_args()
    cap=55 if a.max_n==2 else 300
    out={'max_n':a.max_n,'cases':0,'rows':[],'real_witnesses':[],'units':'bits','data_measure':'uniform'}
    for k in range(-12,13):assert logi(F(2)**k)==(F(k),F(k))
    for n in range(a.max_n+1):
        N=1<<n; tables=[tuple(1 if (m>>x)&1 else -1 for x in range(N)) for m in range(1<<N)]
        W=[walsh(t) for t in tables]
        for w,t in zip(W,tables):
            assert w==direct(t) and sum(u*u for u in w)==N*N and walsh(w)==tuple(N*x for x in t)
            for i in range(n):assert sum(u*u for s,u in enumerate(w) if (s>>i)&1)==N*sum(t[x]!=t[x^(1<<i)] for x in range(N))
        for p in (F(1,8),F(1,4),F(3,8)):
            types=sorted({u for w in W for u in w}); cache={(u,v):fiber(u,v,N,p) for u in types for v in types}
            bestlo=besthi=-100*SCALE; witness=None; lower_holders=[]; possible=[]; scores=[]
            for i,g in enumerate(W):
                if time.monotonic()-CLOCK>cap:raise RuntimeError('frozen runtime cap')
                for j,h in enumerate(W):
                    lo=hi=0
                    for u,v in zip(g,h):fl,fh=cache[u,v];lo+=fl;hi+=fh
                    scores.append((lo,hi,i,j))
                    if lo>bestlo:bestlo=lo;witness=[i,j]
                    besthi=max(besthi,hi)
            candidates=[(i,j) for lo,hi,i,j in scores if hi>=bestlo]
            second=max((hi for lo,hi,i,j in scores if hi<bestlo),default=None)
            g,h=(W[i] for i in witness)
            expression=symbolic_pair(g,h,N,p)
            assert all(symbolic_pair(W[i],W[j],N,p)==expression for i,j in candidates)
            masses=[]
            for u,v in zip(g,h):
                G,H=F(u,N),F(v,N);masses.extend([str(((1-p)*G+p*H)**2),str(p*(1-p)*(H-G)**2)])
            # Same parent selector influence computed physically and spectrally.
            delta=F(sum(u!=v for u,v in zip(tables[witness[0]],tables[witness[1]])),N)
            assert sum(F(x) for x in masses[1::2])==4*p*(1-p)*delta
            row={'n':n,'p':str(p),'pair_count':len(W)**2,'max_debt':record((bestlo,besthi)), 'witness_masks':witness,
                 'candidate_maximizers':len(candidates),'noncandidate_separation_lower':str(F(bestlo-second,SCALE)) if second is not None else None,
                 'exact_max_expression_log2_primes':{str(prime):str(c) for prime,c in expression},'all_candidates_symbolically_equal':True,
                 'witness_child_tables':[tables[witness[0]],tables[witness[1]]],'witness_integer_Walsh':[g,h],'witness_parent_spectrum':masses}
            out['rows'].append(row);out['cases']+=len(W)**2
            (R/'out'/('PILOT.json' if a.max_n==2 else 'CENSUS.json')).write_text(json.dumps(out,indent=2),encoding='utf8')
            print('row',n,str(p),'max',row['max_debt']['display'],'candidates',len(candidates),flush=True)
    for p in (F(1,8),F(1,4),F(3,8)):
        xs={F(1,1<<j) for j in range(2,17) if F(1,1<<j)<=p}|{p/4,p/16,p}
        choices=[real_witness(p,x) for x in sorted(xs)]
        best=max(choices,key=lambda q:q['raw_lower']);best.pop('raw_lower');best['p']=str(p)
        boolrow=next(q for q in out['rows'] if q['n']==a.max_n and q['p']==str(p))
        gap=F(best['debt']['lower'])-F(boolrow['max_debt']['upper'])
        best['gap_above_Boolean_upper']=str(gap);out['real_witnesses'].append(best)
    out['runtime_seconds']=time.monotonic()-CLOCK;out['self_checks']='PASS: direct/inverse Walsh, Parseval, edge influence, selector influence, log2 powers, exact interval max aggregation'
    (R/'out'/('PILOT.json' if a.max_n==2 else 'CENSUS.json')).write_text(json.dumps(out,indent=2),encoding='utf8')
    print('PASS',out['cases'],'runtime',out['runtime_seconds'],'real gaps',[float(F(x['gap_above_Boolean_upper'])) for x in out['real_witnesses']])
if __name__=='__main__':main()
