"""Exact frustrated-cycle witness and phase-sector certificate.

Only rational arithmetic decides the claims: atom determinants/inverses,
atanh-series logarithm enclosures, and the rank-one Schur inequality.
This does NOT claim a Lyons counterexample.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s

OUT=Path(__file__).resolve().parent

def f(x):
    x=s.cancel(x);assert x.is_Rational,x
    return F(int(x.p),int(x.q))

def rawlog(y,N=40):
    assert F(1)<=y<=F(2)
    u=(y-1)/(y+1);v=u;z=F(0)
    for j in range(N):z+=2*v/F(2*j+1);v*=u*u
    return z,z+2*v/(F(2*N+1)*(1-u*u))

LOG2=rawlog(F(2));SCALE=10**30
def logbounds(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    while y<1:y*=2;k-=1
    while y>=2:y/=2;k+=1
    lo,hi=rawlog(y)
    if k>=0:lo+=k*LOG2[0];hi+=k*LOG2[1]
    else:lo+=k*LOG2[1];hi+=k*LOG2[0]
    return F((lo*SCALE).__floor__(),SCALE),F((hi*SCALE).__ceil__(),SCALE)

def linlog(coeff,logs):
    lo=hi=F(0)
    for c,(l,h) in zip(coeff,logs):
        if c>=0:lo+=c*l;hi+=c*h
        else:lo+=c*h;hi+=c*l
    return lo,hi

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [enc(z) for z in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x

def main():
    n=4;z=[s.Rational(3,20),s.Rational(9,50),s.Rational(1,5),-s.Rational(1,1000)]
    K=s.eye(n)/2
    for i in range(n):
        j=(i+1)%n;K[i,j]=K[j,i]=z[i]
    # Gershgorin gives BOTH K and I-K >=3/25 I, exactly.
    row_bounds=[s.Rational(1,2)-sum(abs(K[i,j]) for j in range(n) if i!=j) for i in range(n)]
    assert min(row_bounds)==s.Rational(3,25)
    radial=[];phase=[]
    for i in range(n):
        j=(i+1)%n;R=s.zeros(n);A=s.zeros(n)
        R[i,j]=R[j,i]=z[i];A[i,j]=s.I*z[i];A[j,i]=-s.I*z[i]
        radial.append(R);phase.append(A)
    q=f(s.prod(z));atoms=[]
    for mask in range(16):
        bits=[(mask>>i)&1 for i in range(n)]
        M=K-s.diag(*[1-b for b in bits]);p=f((-1)**(n-sum(bits))*M.det());T=M.inv()
        g=[f(p*(T*R).trace()) for R in radial]
        ph=[T*A for A in phase]
        assert all(X.trace()==0 for X in ph)
        hh=[[f(p*(X.trace()*Y.trace()-(X*Y).trace())) for Y in ph] for X in ph]
        c=F(2*(-1)**(sum(bits)+1))
        # Exact determinant identity behind diag(w)-gamma*11^T.
        for i in range(n):
            for j in range(n):
                assert hh[i][j] == (g[i]-c*q if i==j else -c*q)
        atoms.append({'mask':mask,'p':p,'radial_derivatives':g,'phase_second_derivatives':hh,'cycle_coefficient':c})
    assert sum(a['p'] for a in atoms)==1
    assert all(sum(a['radial_derivatives'][i] for a in atoms)==0 for i in range(n))
    logs=[logbounds(a['p']) for a in atoms]
    wb=[linlog([-a['radial_derivatives'][i] for a in atoms],logs) for i in range(n)]
    hqb=linlog([-a['cycle_coefficient'] for a in atoms],logs)
    gammab=(min(q*hqb[0],q*hqb[1]),max(q*hqb[0],q*hqb[1]))
    assert all(wb[i][1]<0 for i in range(3))
    assert wb[3][0]>0 and gammab[0]>0
    # Complete phase-sector negativity, despite one positive radial weight.
    # If k is the positive edge, diag(w)-gamma 11* <0 iff
    # w_k*(1/gamma+sum_{j!=k}1/(-w_j))<1.
    schur_upper=wb[3][1]*(1/gammab[0]+sum(1/(-wb[i][1]) for i in range(3)))
    assert schur_upper<F(3,4),float(schur_upper)
    gauge_upper=wb[3][1]*sum(1/(-wb[i][1]) for i in range(3))
    # C071 exclusion: normalized C triangle has same sign as -Lij Ljk Lki.
    L=K*(s.eye(n)-K).inv();violations=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                value=f(-L[i,j]*L[j,k]*L[k,i])
                if value<0:violations.append({'triangle':[i,j,k],'unnormalized_C_cycle':value})
    assert violations
    bycount=[[a['p'] for a in atoms if a['mask'].bit_count()==k] for k in range(5)]
    count_ranges=[max(v)-min(v) for v in bycount]
    assert max(count_ranges)>0
    # The phase direction is imaginary while every K edge is real; any
    # nonzero phase direction has no real affine intersection with diagonal.
    result={'status':'exact_obstruction_and_negative_phase_certificate_not_counterexample',
        'K':[[str(v) for v in row] for row in K.tolist()],
        'contraction_margin':'3/25','cycle_product':q,
        'radial_entropy_derivative_bounds':wb,'H_q_bounds':hqb,'gamma_bounds':gammab,
        'positive_radial_edge_index':3,'positive_radial_derivative_lower_simple':'1/25000000',
        'phase_Schur_upper':schur_upper,'phase_Schur_upper_simple':'3/4',
        'gauge_Schur_upper':gauge_upper,'negative_real_odds_triangles':violations,
        'count_probability_ranges':count_ranges,'atoms':atoms,
        'log_method':{'terms':40,'range_reduction':'x=2^k*y, 1<=y<2',
                      'rounding_denominator':str(SCALE)}}
    assert wb[3][0]>F(1,25000000)
    (OUT/'exact_certificate.json').write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps({k:enc(v) for k,v in result.items() if k not in ['atoms','phase_Schur_upper','gauge_Schur_upper']},indent=2))
    print('numerical radial weights:',[sum(map(float,w))/2 for w in wb])
    print('numerical gamma:',sum(map(float,gammab))/2)
    print('rigorous phase Schur upper:',float(schur_upper))

if __name__=='__main__':main()
