"""Exact rational certificate for a proof-method obstruction, NOT a DPP counterexample.

No numerical library or floating point sign is used. Natural logarithms are enclosed
using a rational atanh series and an explicit geometric tail bound.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
from pathlib import Path

def log_unit(x, terms=40):
    assert 1 <= x <= 2
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo,lo+tail

def log_bounds(x):
    assert x>0
    m=0
    while x<1:x*=2;m-=1
    while x>2:x/=2;m+=1
    l,u=log_unit(x);l2,u2=log_unit(F(2))
    return (l+m*l2,u+m*u2) if m>=0 else (l+m*u2,u+m*l2)

def scale(c,I):
    l,u=I
    return (c*l,c*u) if c>=0 else (c*u,c*l)

def enclose_decimal(I,digits=18):
    # Rounded OUTWARDS to rational multiples of 10^-digits.
    scale10=10**digits;l,u=I
    low=(l.numerator*scale10)//l.denominator
    high=-((-u.numerator*scale10)//u.denominator)
    return [str(F(low,scale10)),str(F(high,scale10))]

def polynomial_table(e=F(1,10)):
    p=[F(3,4),F(3,4),F(1,4),F(1,4)];v=[1,-1,0,0]
    perms=[[0,1,2,3],[1,0,2,3],[2,3,0,1]]
    weights=[(1-e)/2,(1-e)/2,e]
    rows={s:[F(0)]*3 for s in product([0,1],repeat=4)}
    for s in rows:
        a=[F(1),F(0),F(0)]
        for i in range(4):
            f=p[i] if s[i] else 1-p[i]
            d=F(v[i] if s[i] else -v[i])
            a=[a[0]*f,a[1]*f+a[0]*d,a[2]*f+a[1]*d]
        for perm,w in zip(perms,weights):
            y=tuple(s[i] for i in perm)
            rows[y]=[q+w*x for q,x in zip(rows[y],a)]
    assert [sum(q[j] for q in rows.values()) for j in range(3)]==[1,0,0]
    return rows

def entropy_interval(rows,t):
    lo=hi=F(0)
    for a,b,c in rows.values():
        p=a+b*t+c*t*t;assert p>0
        l,u=scale(-p,log_bounds(p));lo+=l;hi+=u
    return lo,hi

def main():
    rows=polynomial_table();fi=sum(b*b/a for a,b,c in rows.values())
    assert fi==F(1048,3075)
    logs=defaultdict(F)
    for a,b,c in rows.values():logs[a]+=2*c
    assert dict((p,c) for p,c in logs.items() if c)=={F(9,256):F(1,40),F(27,1280):F(-3,10),F(123,1280):F(13,10),F(73,256):F(-41,40)}
    qlo=qhi=fi
    for p,c in logs.items():
        l,u=scale(c,log_bounds(p));qlo+=l;qhi+=u
    assert qhi < -F(1,3)
    h0=entropy_interval(rows,F(0));hp=entropy_interval(rows,F(1,100));hm=entropy_interval(rows,-F(1,100))
    gap=((hp[0]+hm[0])/2-h0[1],(hp[1]+hm[1])/2-h0[0])
    assert gap[0] > F(1,60000)
    mean1=sum(a for s,(a,b,c) in rows.items() if s[0]);mean2=sum(a for s,(a,b,c) in rows.items() if s[1]);both=sum(a for s,(a,b,c) in rows.items() if s[0] and s[1])
    cov=both-mean1*mean2
    assert cov==F(9,400)>0
    result=dict(status='PASS: enlarged-channel obstruction only; Lyons remains OPEN',epsilon='1/10',parameters=['3/4+t','3/4-t','1/4','1/4'],curvature_interval=enclose_decimal((qlo,qhi)),entropy_second_derivative_lower_bound='1/3',finite_endpoint_t='1/100',jensen_violation_interval=enclose_decimal(gap),jensen_violation_lower_bound='1/60000',covariance_12=str(cov),series_terms=40,atom_polynomials=[dict(bits=''.join(map(str,s)),coefficients=list(map(str,q))) for s,q in rows.items()])
    Path('shuffle_obstruction_certificate.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='atom_polynomials'},indent=2))

if __name__=='__main__':main()
