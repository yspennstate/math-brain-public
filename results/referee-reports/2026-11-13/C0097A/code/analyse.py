#!/usr/bin/env python3
"""Exact, small, single-threaded coefficient checks for C0097. Standard library only."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import csv, json, time, resource
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
# CLS (2007), equation (1), author pp. 3-4. mu=s^-1+sum a[k]*s^k.
A = [-1,-1,-3,-16,-102,-729,-5533,-42229,-288761,-1026328,21070667,780280468]

def mul(a,b,n):
    out=[F(0)]*(n+1)
    for i,x in enumerate(a[:n+1]):
        if x:
            for j,y in enumerate(b[:n+1-i]):
                if y: out[i+j]+=x*y
    return out

def inverse(a,n):
    assert a[0]
    out=[1/F(a[0])]
    for k in range(1,n+1):
        out.append(-sum(F(a[j])*out[k-j] for j in range(1,min(k,len(a)-1)+1))/a[0])
    return out

def csv_write(name,fields,rows):
    with (DATA/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def saw():
    # mu = s^-1*m(s), beta=s/m(s), so 13 beta coefficients are known.
    m=[1]+A
    inv=inverse(m,12)
    beta=[F(0)]+inv
    assert mul(m,inv,12)==[1]+[0]*12
    assert beta[1:7]==[1,1,2,6,27,157]
    rows=[]
    for k,a in enumerate(A):
        rows.append(dict(k=k,a_k=a,abs_ratio='' if not k else float(F(abs(a),abs(A[k-1]))),
                         ratio_over_k='' if not k else float(F(abs(a),k*abs(A[k-1]))),
                         nth_root='' if not k else abs(a)**(1/k),
                         borel_coefficient=str(F(a,factorial(k))),
                         borel_abs_ratio='' if not k else float(F(abs(a),k*abs(A[k-1])))))
    csv_write('saw_mu.csv',list(rows[0]),rows)
    rows=[]
    for n,a in enumerate(beta[1:],1):
        rows.append(dict(n=n,alpha_n=str(a),abs_ratio='' if n==1 else float(abs(a/beta[n-1])),
                         borel_coefficient=str(a/factorial(n)),
                         borel_abs_ratio='' if n==1 else float(abs(a/beta[n-1])/n)))
    csv_write('saw_beta.csv',list(rows[0]),rows)
    # An independent reciprocal check: beta_n=-sum m_j beta_{n-j}.
    recurrence=[F(0),F(1)]
    for n in range(2,14):
        recurrence.append(-sum(F(m[j])*recurrence[n-j] for j in range(1,n)))
    assert recurrence==beta
    trunc=[]
    for d in [1,2,3,5,10]:
        s=F(1,2*d);val=1/s
        for k,a in enumerate(A):
            val+=a*s**k
            trunc.append(dict(d=d,last_power=k,mu_partial=str(val),mu_partial_decimal=float(val)))
    csv_write('saw_partial_sums.csv',list(trunc[0]),trunc)
    print('SAW a_0..a_11:',A)
    print('SAW alpha_1..alpha_13:',[int(x) for x in beta[1:]])
    return beta

def srw_lagrange(N):
    # g=x-log I0(x); h=g^-1. Lagrange: b_n=[x^(n-1)](x/g)^n/n.
    i0=[F(0)]*(N+1);i0[0]=F(1)
    for k in range(1,N//2+1):i0[2*k]=F(1,4**k*factorial(k)**2)
    logi=[F(0)]*(N+1)
    for n in range(1,N+1):
        logi[n]=i0[n]-sum((F(k)*logi[k]*i0[n-k] for k in range(1,n)),F(0))/n
    g=[-v for v in logi];g[1]+=1
    w=inverse(g[1:],N-1)
    power=[F(1)]+[F(0)]*(N-1)
    h=[F(0)]
    for n in range(1,N+1):
        power=mul(power,w,N-1)
        h.append(power[n-1]/n)
    assert all(isinstance(x,F) for x in h)
    gamma=[2**m*factorial(m+1)*h[m+1] for m in range(N)]
    assert all(isinstance(x,F) for x in gamma)
    return h,gamma

def srw_closed_walks(M):
    # Independent enumeration by occupied coordinate axes.
    # C_(2n)(d)=(2n)! sum_k binom(d,k) [x^n](sum_(j>=1) x^j/(j!)²)^k.
    f=[F(0)]+[F(1,factorial(j)**2) for j in range(1,M+1)]
    powers=[[F(1)]+[F(0)]*M]
    for k in range(1,M+1):powers.append(mul(powers[-1],f,M))
    out=[F(1)]+[F(0)]*M
    for n in range(1,M+1):
        for k in range(1,n+1):
            base=F(factorial(2*n),2**k*factorial(k))*powers[k][n]
            prod=[1]
            for j in range(k):prod=mul(prod,[1,-2*j],len(prod))
            shift=2*n-k
            for j,v in enumerate(prod):
                if shift+j<=M:out[shift+j]+=base*v
    return out

def srw():
    h,gamma=srw_lagrange(40)
    assert gamma[:13]==srw_closed_walks(12)
    assert gamma[:5]==[1,1,3,12,60]
    pinv=inverse(gamma,39)
    ret=[F(0)]+[-x for x in pinv[1:]]
    assert ret[:6]==[0,1,2,7,35,215]
    rows=[]
    for m,c in enumerate(gamma):
        rows.append(dict(m=m,green_coefficient=str(c),return_coefficient=str(ret[m]),
                         inverse_g_coefficient=str(h[m+1]),
                         green_borel_coefficient=str(c/factorial(m))))
    csv_write('srw.csv',list(rows[0]),rows)
    # Elementary verification that I0 has two omitted values for Picard argument.
    j0_upper=sum(F((-9)**k,4**k*factorial(k)**2) for k in range(5))
    assert j0_upper<0
    print('J0(3) < even partial sum =',j0_upper)
    print('SRW gamma_0..gamma_12:',[int(x) for x in gamma[:13]])
    return str(j0_upper)

if __name__=='__main__':
    start=time.monotonic();DATA.mkdir(exist_ok=True)
    saw();bound=srw()
    (DATA/'analysis_checks.json').write_text(json.dumps(dict(
        saw_reciprocal_product='exact through normalized degree 12',
        saw_reciprocal_independent_recurrence=True,
        srw_lagrange_vs_closed_walks='exact through degree 12',
        srw_return_initial_coefficients=[0,1,2,7,35,215],
        J0_3_rigorous_upper_bound=bound,
        seconds=time.monotonic()-start,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        threads=1),indent=2)+'\n')
    print('all exact checks passed; elapsed',round(time.monotonic()-start,3),'s')
