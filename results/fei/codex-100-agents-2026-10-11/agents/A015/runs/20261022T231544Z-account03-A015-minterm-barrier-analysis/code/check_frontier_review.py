"""Independent rational reconstruction; no import of A007 or main checker."""
from fractions import Fraction as F
from pathlib import Path
from math import comb, prod
import hashlib
import json
import time

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();count=0
def ck(ok,why):
    global count
    count+=1
    if not ok:raise AssertionError(why)
    if time.monotonic()-start>20:raise RuntimeError('Frozen time limit')

for k in range(1,129):
    a=F(comb(2*k,k),4**k);q=(1+a)/2
    ratio=4*q*(1-q*q)/a
    ck(a*a*(k+1)<=1,('central binomial bound',k))
    ck(F(1,2)<=q<=F(3,4),('central q',k))
    ck(ratio*ratio>=F(49,64)*(k+1),('dimension barrier',k))
    next_a=F(comb(2*k+2,k+1),4**(k+1))
    ck(next_a/a==F(2*k+1,2*k+2),('binomial recursion',k))
    ck(F(2*k+1,2*k+2)**2<=F(k+1,k+2),('induction',k))

for m in range(2,129):
    a=F(1,2**m);b=(1-a)**2
    ck(m*a<=F(1,2),('ma',m))
    ck(m*m*a<=F(9,8),('m2a',m))
    ck(b>=F(9,16),('controller bank',m))
    # Source has log2(m)<=m; this stronger exact bound uses m directly.
    ck(m*a*(4*m+F(211,10))/b+F(63,40)<29,('source bound 29',m))
ck((4*F(9,8)+F(211,10)*F(1,2))/F(9,16)+F(63,40)==F(10199,360),
   'source combined constant')

w=[F(1,8),F(1,9),F(1,12)];degrees=[1,2,3]
root_weights=[F(1,8),F(1,12),F(1,24)]
alpha=F(1,4);fixtures=[]
for r in range(1,4):
    p=F(1,2**r);invariant=None
    for t in [F(1),F(1,2),F(1,4)]:
        beta=alpha/t
        Dt=prod(1+t*z for z in root_weights)-1
        Dprime=prod(1+p*alpha*z for z in root_weights)-1
        St=sum(t**k*a for k,a in zip(degrees,w))
        eta=[t**k*a/St for k,a in zip(degrees,w)]
        J=[];N=[]
        for U in range(1<<r):
            u=U.bit_count()
            H=[F((k+1)**u)*(1+F(u,7)) for k in degrees]
            j=sum(e*beta**k*h for e,k,h in zip(eta,degrees,H))
            nn=sum(alpha**k*a*h for k,a,h in zip(degrees,w,H))
            ck(St*j==nn,('record identity',r,str(t),U))
            J.append(j);N.append(nn)
        # Exponentiate (p R_t + Psi)/p^2: all exponents are integers.
        lhs=((Dt/St)*(Dprime/(p*Dt)))**(1<<r)/prod(J)
        rhs=(Dprime/p)**(1<<r)/prod(N)
        ck(lhs==rhs,('signed normalization cancellation',r,str(t)))
        if invariant is None:invariant=lhs
        ck(lhs==invariant,('same final scale',r,str(t)))
        if t!=1:
            ck(eta!=[a/sum(w) for a in w],('posterior changes',r,str(t)))
        fixtures.append({'r':r,'t':str(t),'beta':str(beta),'exponentiated_cost':str(lhs)})

result={'status':'PASS','assertions':count,'central_cases':128,'payment_cases':127,
        'scale_cases':9,'scale_fixtures':fixtures,'elapsed_seconds':round(time.monotonic()-start,3),
        'scope':'New central analytic proof validation; A007 new numerical payment and scale cancellation only. No reacceptance of A015 own upstream theorem or A007 sharp asymptotic.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'frontier_review.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','assertions','elapsed_seconds']}))
