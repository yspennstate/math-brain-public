"""Exponent-safe full matching-tower profiles; no binary64 tail truncation."""
from decimal import Decimal as D, localcontext
import argparse,json,resource,time
import numpy as np
from levels import ROOT,wht,pm33

ZERO=D(0);ONE=D(1)

def convolution(a,b):
    out=[ZERO]*(len(a)+len(b)-1)
    aa=[(i,x) for i,x in enumerate(a) if x]
    bb=[(j,y) for j,y in enumerate(b) if y]
    for i,x in aa:
        for j,y in bb:out[i+j]+=x*y
    return out

def add_scaled(target,src,scale,offset=0):
    if not scale:return
    for i,x in enumerate(src):target[i+offset]+=scale*x

def run(precision,max_depth):
    began=time.monotonic();outer=[D.from_float(float(x)) for x in wht(pm33())]
    W=[ZERO,ONE];A=[ZERO,ZERO];a=ZERO;c=ONE;n=1;rows=[]
    ln2=D(2).ln()
    for depth in range(1,max_depth+1):
        b=outer.copy()
        for j in range(9):
            for s in range(512):
                if not s>>j&1:b[s]+=a*b[s|(1<<j)]
        bydegree=[[s for s in range(512) if s.bit_count()==r] for r in range(10)]
        Bs=[sum((b[s]*b[s] for s in ss),ZERO) for ss in bydegree]
        Cs=[ZERO]*10;q=c*c
        for r in range(1,10):
            for s in bydegree[r]:
                if b[s] and q:
                    for j in range(9):
                        if s>>j&1:Cs[r]+=D(n)*q*b[s]*b[s]*(ONE+b[s^(1<<j)]**2/(b[s]*b[s]*q)).ln()/ln2
        P=W.copy();P[0]=ZERO;powers=[[ONE]]
        for r in range(1,10):powers.append(convolution(powers[-1],P))
        wn=[ZERO]*(9*n+1);an=[ZERO]*(9*n+1);deriv=[ZERO]*(8*n+1)
        for r in range(10):
            add_scaled(wn,powers[r],Bs[r])
            if r:
                add_scaled(deriv,powers[r-1],D(r)*Bs[r])
                add_scaled(an,powers[r-1],Cs[r],1)
        aint=A.copy();aint[1]=ZERO
        interior=convolution(aint,deriv);add_scaled(an,interior,ONE)
        n*=9;W=wn;A=an;a=b[0];c*=b[1]
        norm=sum(W,ZERO);I=sum((D(d)*w for d,w in enumerate(W)),ZERO);G=sum(A,ZERO)
        assert abs(norm-ONE)<D(10)**(-precision+7)
        assert abs(W[0]-a*a)<D(10)**(-precision+7)
        assert abs(W[1]-D(n)*c*c)<D(10)**(-precision+7)
        maxes={key:dict(ratio=ZERO,d=0) for key in ['L1','L2','lower_all','tail_linear','global_I']}
        cumulative=ZERO;tail=[ZERO]*(n+1);running=ZERO
        for d in range(n,-1,-1):tail[d]=running;running+=D(d)*W[d]
        for d in range(n+1):
            lower=cumulative;cumulative+=W[d]
            if d<2:continue
            den1=D(d)*W[d]+D(d-1)*W[d-1]
            dens=dict(L1=den1,L2=D(d)*W[d]+W[d-1],lower_all=D(d)*W[d]+lower,
                      tail_linear=den1+tail[d],global_I=I)
            for key,den in dens.items():
                assert den or not A[d]
                ratio=A[d]/den if den else ZERO
                if ratio>maxes[key]['ratio']:maxes[key]=dict(ratio=ratio,d=d)
        for key in maxes:maxes[key]['ratio']=str(maxes[key]['ratio'])
        row=dict(depth=depth,n=n,precision_decimal_digits=precision,mean=str(a),singleton=str(c),
            W=[str(x) for x in W],A=[str(x) for x in A],I=str(I),G=str(G),
            min_positive_W=str(min(x for x in W if x)),maxima=maxes,
            probability_mass_error=str(norm-ONE),elapsed_seconds=time.monotonic()-began)
        rows.append(row)
        (ROOT/f'towers_decimal_{precision}.json').write_text(json.dumps(rows,indent=2))
        print(depth,n,'I',I,'G',G,'mass_error',norm-ONE,'seconds',time.monotonic()-began,flush=True)
    (ROOT/f'towers_decimal_{precision}_resources.json').write_text(json.dumps(dict(
        max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,elapsed_seconds=time.monotonic()-began),indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--precision',type=int,default=40);p.add_argument('--depth',type=int,default=4);a=p.parse_args()
    with localcontext() as ctx:ctx.prec=a.precision;run(a.precision,a.depth)
