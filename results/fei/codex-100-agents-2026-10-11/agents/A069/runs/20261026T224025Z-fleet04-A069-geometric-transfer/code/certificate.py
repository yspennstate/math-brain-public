"""Exact finite checks for the analytic near-Boolean route guard; no huge n allocated."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse, hashlib, json, time

RUN=Path(__file__).resolve().parents[1]
checks=0
def check(pred):
    global checks
    checks+=1
    if not pred: raise AssertionError(checks)

def fwht(values):
    a=list(values); h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return [v/len(a) for v in a]

def main(pilot=False):
    start=time.perf_counter(); rows=[]
    for m in ([2] if pilot else [2,4,8]):
        n=m*m; p=F(1,n+1); r=1-2*p
        weights={s:p**s*(1-p)**(n-s) for s in range(1,n+1,2)}
        A=sum((comb(n,s)*w for s,w in weights.items()),F(0))
        J=sum((s*comb(n,s)*w for s,w in weights.items()),F(0))
        check(A==(1-r**n)/2); check(J==n*p*(1+r**(n-1))/2)
        check(F(1,3)<A<F(1,2)); check(0<J<=1)
        check((1+F(2,n-1))**n>=1+F(2*n,n-1)>3)
        for w in weights.values(): check(0<w<=p)
        for eps in [F(1,2),F(1,4),F(1,8)]:
            Z=1+eps*eps*A
            mass=1/Z+sum(comb(n,s)*eps*eps*w/Z for s,w in weights.items())
            energy=(1+eps*eps*J)/Z
            check(mass==1); check(0<energy<=1+eps*eps)
            for w in weights.values(): check(0<eps*eps*w/Z<=p)
            check((1+eps)**2/Z-1<=2*eps+eps*eps)
            check(1-(1-eps)**2/Z<=2*eps+eps*eps)
            # Rational entropy lower bound coefficient; log(n+1) remains symbolic.
            coefficient=eps*eps*A/(1+eps*eps*J)
            check(coefficient>eps*eps/(3*(1+eps*eps)))
            rows.append(dict(n=n,epsilon=str(eps),A=str(A),J_h=str(J),J_g=str(energy),entropy_ratio_log_coefficient=str(coefficient)))
    # Independent direct physical implementation for h_4, all inputs.
    m=2; n=4; den=(m*m+1)**(n//2); table=[]
    for x in range(1<<n):
        re,im=1,0
        for j in range(n):
            y=1 if not (x>>j)&1 else -1
            re,im=m*re-y*im,y*re+m*im
        check(re*re+im*im==den*den)
        check(abs(im)<=den)
        table.append(F(im,den))
    coeff=fwht(table)
    for S,a in enumerate(coeff):
        s=S.bit_count()
        expected=F((-1)**((s-1)//2)*m**(n-s),den) if s%2 else F(0)
        check(a==expected)
    h2coeff=fwht([v*v for v in table])
    for T in range(16):
        check(sum(coeff[S]*coeff[S^T] for S in range(16))==h2coeff[T])
    for eps in [F(1,2),F(1,4),F(1,8)]:
        A=sum(v*v for v in coeff); Z=1+eps*eps*A
        # g's normalized square is rational even though g itself has sqrt(Z).
        square=[(F(1 if x0==0 else -1)+eps*v)**2/Z for x0 in range(2) for v in table]
        raw=[F(1 if x0==0 else -1)+eps*v for x0 in range(2) for v in table]
        raw_coeff=fwht(raw)
        check(sum(v*v/Z for v in raw_coeff)==1)
        for x,v in enumerate(raw): check(v>0 if x<16 else v<0)
        residual=fwht([v-1 for v in square])
        check(residual[0]==0)
        check(sum(v*v for v in residual)<= (2*eps+eps*eps)**2)
        # Every physical restriction, including constants: 3^5 states.
        for state in range(3**5):
            spec=state; pattern=[]
            for j in range(5): pattern.append(spec%3); spec//=3
            indices=[x for x in range(32) if all(a==0 or ((x>>j)&1)==a-1 for j,a in enumerate(pattern))]
            norm=sum(square[x] for x in indices)/len(indices)
            check(abs(norm-1)<=2*eps+eps*eps)
    # A070's physical versus separately normalized child means.
    check((F(1)+F(1,9))/2==F(5,9))
    check((F(9,13)+F(1,5))/2==F(29,65))
    check(F(29,65)!=F(5,9))
    check((F(4,13)+F(4,5))/2==F(36,65))
    check(F(5,9)-F(29,65)==F(64,585))
    # h2(1/5)<=1, log2(4095)>11: exact strict negative guard.
    check(4095>2**11); check(F(64,585)*11>1)
    # Explicit infinite-family parameter lower bound uses n only via log2 n.
    for k in [2,3,4,8,16,32]:
        eps=F(1,k); log_n=2*k**4
        lower=eps*eps*log_n/(3*(1+eps*eps))
        check(lower==F(2*k**4,3*(k*k+1)))
        check(2*eps+eps*eps>0)
    out=dict(status="PASS",rung="exact finite rational certificate plus separate analytic proof",checks=checks,rows=rows,physical_restrictions=3*3**5,elapsed_seconds=time.perf_counter()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),not_boolean_counterexample=True)
    name="pilot.json" if pilot else "results.json"
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','checks','physical_restrictions','elapsed_seconds','not_boolean_counterexample']}))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args(); main(args.pilot)
