#!/usr/bin/env python3
"""Directed fixed-point convolution with exact GMP multiplication.

python3 -m pip install --target code/vendor gmpy2 python-flint
No FFT rounding: Kronecker substitution packs polynomial coefficients in base
2^blockbits. All probability coefficients are rounded downward. Arb certifies
initial coefficient floors; integer arithmetic propagates a weighted Wasserstein
error bound. See REPORT.md for the proof of the bound.
"""
import os,sys,argparse,csv,json,time,resource
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
sys.path.insert(0,str(Path(__file__).parent/'vendor'))
import gmpy2 as g
from flint import arb,ctx
BITS=112; S=1<<BITS; EBITS=192; R=1<<EBITS
ctx.prec=240
if hasattr(ctx,"threads"):ctx.threads=1

def floorball(x):
    y=x.floor().unique_fmpz()
    if y is None: raise ArithmeticError('initial floor not certified')
    return int(y)

def init(m,law,K):
    a=[0]*(K+1)
    if law.startswith('two'):
        h=int(law[3:]); a[h]=(S*m**h)//(1+((m-1)*h-1)*m**h)
        count=1
    elif law=='geom':
        # c=(2m-1)/(4(m-1)^2), a_k/S=c*2^-k.
        base=(S*(2*m-1))//(4*(m-1)**2)
        for k in range(1,K+1):a[k]=base>>k
        count=K
    elif law=='sparse':
        A=(m-1)*arb(2).zeta()-(arb(1)/2).polylog(2)
        T=sum((arb(m)**(-(2**j)))/(j*j*2**j) for j in range(1,17))
        tail=arb(m)**(-(2**17))*arb(2)**(-16)/(17**2)
        c=1/(A+T+arb(0,tail))
        count=0
        for j in range(1,K.bit_length()):
            h=2**j
            if h<=K:a[h]=floorball(S*c/(j*j*h));count+=1
    elif law.startswith('power'):
        b=arb(law[5:])
        # Use the exact rational 1/m in polylog, rather than binary64 1/m.
        c=1/((m-1)*(b-1).zeta()-b.zeta()+(arb(1)/m).polylog(b))
        for k in range(1,K+1):a[k]=floorball(S*c/arb(k)**b)
        count=K
    else:raise ValueError(law)
    return a,count*(R//S)

def ceil_survival_scaled(a,m):
    v=0
    for x in reversed(a[1:]):v=(v+x+m-1)//m
    return v

def run(m,law,N,K,out):
    start=time.time();a,e=init(m,law,K);W=16*m # bytes, blockbits=128*m
    rows=[];Rp=R**(m-1); delta=(K+m)*(R//S)
    def record(n,v):
        # These rational endpoints exclude support error; an additional exact
        # support bound, with B replaced by the integer m, is added in analysis.
        lo=max(0,v-1); upper_num=v*R+(e*S+m-2)//(m-1)
        rows.append({'n':n,'q_mid':(v-0.5)/S,'n2q':n*n*(v-0.5)/S,
                     'q_lower_numerator':lo,'q_lower_denominator':S,
                     'q_upper_numerator':upper_num,'q_upper_denominator':S*R,
                     'rounding_error_bound':e/R/(m-1),
                     'tilted_mass_upper':1+sum(a)/S})
    v=ceil_survival_scaled(a,m);record(0,v)
    for n in range(1,N+1):
        total=sum(a)
        M=R+(total<<(EBITS-BITS))
        e=(e*(M+e)**(m-1)+Rp-1)//Rp+delta
        p0=S-v
        coeff=[p0]+a[1:]
        # Sum of all coefficients bounds each coefficient of the power.
        assert sum(coeff)**m < 1<<(8*W)
        packed=g.mpz.from_bytes(b''.join(x.to_bytes(W,'little') for x in coeff),'little')
        product=packed**m
        raw=product.to_bytes((m*K+1)*W,'little')
        denom=m*S**(m-1)
        a=[0]+[int.from_bytes(raw[(k+1)*W:(k+2)*W],'little')//denom for k in range(1,K+1)]
        v=ceil_survival_scaled(a,m)
        if n<=10 or n%50==0 or n==N or n&(n+1)==0:record(n,v)
        if n%1000==0:print(m,law,n,n*n*(v-0.5)/S,e/R,flush=True)
    out=Path(out)
    with out.open('w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    out.with_suffix('.json').write_text(json.dumps(dict(m=m,law=law,N=N,K=K,bits=BITS,
        error_bits=EBITS,arb_bits=ctx.prec,block_bits=8*W,seconds=time.time()-start,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        rounding_error_bound=e/R/(m-1),threads=1),indent=2)+'\n')
    print('done',out,time.time()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,required=True);p.add_argument('--law',required=True)
    p.add_argument('--N',type=int,default=10000);p.add_argument('--K',type=int);p.add_argument('--out',required=True)
    args=p.parse_args()
    if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10)
    run(args.m,args.law,args.N,args.K or args.N+128,args.out)
