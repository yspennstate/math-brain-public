from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial, log2
from decimal import Decimal, localcontext
import argparse, json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
start=time.monotonic(); count=0
def ck(x):
    global count
    assert x
    count+=1
def fwht(a):
    a=a[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a
rows=[]
for m in range(2,7 if args.pilot else 41):
    a=Q(1,2**m); I=4*m*a*(1-a); v=4*(1-a)**2*(2*a-a*a)
    within_mass=8*a*(1-a)**2*(1-a)
    cross_mass=4*a*a*(1-a)**2
    ck(within_mass+cross_mass==v)
    within_degree=4*m*a*(1-a)**2
    cross_degree=4*m*a*a*(1-a)
    ck(within_degree+cross_degree==I)
    Mlo=sum((Q(8)*a*a*(1-a)**2*comb(m,s)*(s-1) for s in range(1,m+1)),Q(0))
    ck(Mlo==4*a*(1-a)**2*(m-2+2*a))
    ck(Mlo/I==(1-a)*(m-2+2*a)/m)
    D=(1+Q(1,4*m))**(m*m)-1
    Dp=(1+Q(1,8*m*m))**(m*m)-1
    ck(D>0 and Dp>=Q(1,8) and Dp<=D/(2*m))
    ck(v/(2*I)==(1-a)*(2-a)/(2*m))
    # Every within-side gate owns one coordinate, kappa=1; formal fifth powers.
    for s in range(1,m+1):
        Z5=s**5*Q(1,2**(6*(s-1)))
        rooted5=(factorial(s-1)*4**(s-1))**5
        J5=Q(1,m**(5*s))*Z5*rooted5
        ck(J5==Q(factorial(s)**5*2**(4*(s-1)),m**(5*s)))
    # All edge congestion types. w0>=1/9; w1>=1/2. Check fifth powers exactly.
    for owned,kappa in [(1,1),(1,2),(2,2)]:
        w05=Q(owned,kappa+1)**(6*owned)/Q(owned,kappa)**(6*owned)
        w15=Q(owned+1,kappa+1)**(6*(owned+1))/Q(owned,kappa)**(6*owned)
        ck(Q(1,9)**5<=w05<=1)
        ck(Q(1,2)**5<=w15<=1)
    if m>=4:
        ck(8*m<=2**(m+1)); ck(Q(m+1,2**m)<=Q(5,16))
        ck((Q(2,m)+Q(3,8))/(1-a)<=Q(14,15))
        ck((1-a)/4>=Q(15,64))
    if m <= (3 if args.pilot else 7):
        N=1<<(2*m); mask=(1<<m)-1
        truth=[1 if (x&mask) and (x>>m) else -1 for x in range(N)]
        W=fwht(truth)
        ck(sum(x*x for x in W)==N*N)
        infl=sum(truth[x]!=truth[x^(1<<j)] for x in range(N) for j in range(2*m))
        ck(Q(infl,N)==I)
        ck(Q(sum(s.bit_count()*z*z for s,z in enumerate(W)),N*N)==I)
        ck(1-Q(W[0],N)**2==v)
        for s,z in enumerate(W):
            if not s: continue
            one_side=(s&mask)==0 or (s>>m)==0
            ck(abs(Q(z,N))==(2*a*(1-a) if one_side else 2*a*a))
    # Decimal values are diagnostics for exact within and normalization terms only.
    # Cross remainder is bounded analytically, never replaced by an invented posterior.
    with localcontext() as ctx:
        ctx.prec=65
        dec=lambda x: Decimal(x.numerator)/Decimal(x.denominator)
        lg=lambda x: x.ln()/Decimal(2).ln()
        B=sum((Decimal(comb(m,s))*lg(Decimal(factorial(s))) for s in range(m+1)),Decimal(0))/Decimal(2**m)
        within=(1-dec(a))/(2*m)*(m*lg(Decimal(m))-B-Decimal(4)/5*(Decimal(m)/2-1+dec(a)))
        norm=dec(v/(2*I))*lg(2*dec(Dp)/dec(D))
        err=dec(a*(1-a))*lg(Decimal(9*m))
        rows.append({'m':m,'within_plus_normalization':str(within+norm),
                     'cross_absolute_bound':str(err),'asymptote':str(lg(Decimal(m))/4+Decimal(1)/20)})
    ck(time.monotonic()-start<55)
out={'status':'PASS','assertions':count,'pilot':args.pilot,'seconds':time.monotonic()-start,
     'physical_m':list(range(2,4 if args.pilot else 8)),
     'compressed_m_max':6 if args.pilot else 40,'diagnostics_not_certificates':rows,
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=ROOT/'out'/('pilot.json' if args.pilot else 'checks.json'); dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='diagnostics_not_certificates'}))
