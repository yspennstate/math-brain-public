"""Exact checks for the finite-template cross-entropy repair, frozen separately."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time

root=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0; rows=[]
def ck(v):
    global checks
    checks+=1
    assert v, checks
    assert time.monotonic()-start<60

for m in range(8,13):
    d=Q(2,1<<m); L=(1<<(m-1))//m; N=m*L; u=Q(2,1<<N)
    # Aggregate only truly identical amplitudes, retaining their exact multiplicities.
    p=[]; q=[]; multiplicities=[]
    for r in range(L+1):
        old=(1-d)**(L-r)*(-d)**r
        new=old-(-1)**L*u
        mult=comb(L,r)*((1<<m)-1)**r
        ck(old**2>=d**(2*L))
        p.append(new**2); q.append(old**2); multiplicities.append(mult)
    ck(sum(c*x for c,x in zip(multiplicities,p))==1)
    ck(sum(c*x for c,x in zip(multiplicities,q))==1)
    tv=sum(c*abs(x-y) for c,x,y in zip(multiplicities,p,q))/2
    ck(tv*tv<=Q(4,1<<N))
    # Proved TV bound eta can be irrational; square only nonnegative sides.
    ck((2*N)**2*Q(4,1<<N)<Q(1,16)**2)
    ck(2*L*(m-1)<=2*N)
    ck(Q(69,16)<5*N*(d-u))
    # Dual characterization TV bounds every [0,1] rank-cell score.
    # These include nonconstant scores, and the sign maximizer gives equality.
    for mod in [2,3,5,7]:
        score=[Q(r%mod,mod-1) for r in range(L+1)]
        delta=sum(c*(x-y)*s for c,x,y,s in zip(multiplicities,p,q,score))
        ck(abs(delta)<=tv)
    maximizer=[int(x>y) for x,y in zip(p,q)]
    ck(sum(c*(x-y)*s for c,x,y,s in zip(multiplicities,p,q,maximizer))==tv)
    rows.append({'m':m,'L':L,'N':N,'rank_cells':L+1})

# Guards: a zero reference atom can make KL infinite after a single truth flip;
# a noninvertible affine map can insert a zero direction, violating a>0.
parity=[1,-1,-1,1]; flipped=[-1,-1,-1,1]
old_empty=Q(sum(parity),4)**2; new_empty=Q(sum(flipped),4)**2
ck(old_empty==0 and new_empty>0)  # actual Boolean reference-support failure
ck(0<Q(2,8)-Q(2,64))  # zero directional influence is below the admissible floor
result={'status':'PASS','checks':checks,'rows':rows,'elapsed_seconds':time.monotonic()-start,
        'arithmetic':'Fraction; positive-side squaring; all rank multiplicities retained',
        'scope':'finite-template TV dual and initial full CE source; all-m inequality is analytic'}
(root/'out/REPAIR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
